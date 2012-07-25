import sys
import socket
import re
import threading
import asyncore
import asynchat
import StringIO

import logger
from SMS import SMS, SMSPipelineElement

class AndroidSMS(SMSPipelineElement):
        
    
    def __init__(self, host, port):
        
        SMSPipelineElement.__init__(self, 'android connector', 'android device')
        self.port = port
        self.host  = host
        
        #lets try to connect
        android_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        android_socket.connect((self.host, self.port))      
        logger.log(self, "connected to android device on on host %s port %d" % (host, port))
        
        self.out_ = android_socket.makefile(mode = 'w')
        self.in_ = android_socket.makefile()
        self.socket_ = android_socket
        self.closed = False
        
        self.text_parser = TextParser(self.in_)       
    
    def send(self, sms):        
        try:
            self.out_.write(str(sms))
            self.out_.flush()
        except socket.error as e:
            logger.log_error(self, "Error writing to android socket")
        else:
            logger.log_send(self, sms)
    
    def listen(self): 
        try:
            sms = self.text_parser.one()
        except RuntimeError as e:
            logger.log_error(self, e.message)
            return False
                    
        if sms is None:
            logger.log_error(self, "Connection to android device is broken")
            logger.log_error(self, "Exiting read loop, closing socket")
            self.cleanup()
            return False
        
        logger.log_receive(self, sms)
        self.receive_callback(sms)
        
    def cleanup(self):
        if not self.closed:
            self.socket_.shutdown(socket.SHUT_RDWR)
            self.socket_.close()
            self.closed = True
            
            
class TextParser:
    
    headerParser = re.compile(r"(TO|FROM|LENGTH):(.*)")
    
    def __init__(self, file_):
        
        self.file_ = file_
    

    def one(self):
        """
        copied from java :/
        """
        state = "waiting"
        
        length = 0;
        bodyLinesRemaining = 0;

        to_ = ""
        from_ = ""
        body = ""

        while True: 
                
            try:
                line = self.file_.readline()
            except IOError as e:
                # in socket closed, so return null
                return None

            if line == "": #EOF
                return None
                        
            # ok we did our end of file check, so
            # lets strip off the new line
            line = line.strip()

            # waiting mode
            if state == "waiting":
                
                if line == "TEXT":
                    state = "headers"
                else:
                    # then this was an invalid input for waiting mode!
                    raise RuntimeError("Invalid line while waiting for text: %s" % line);
                
            # HEADER MODE
            elif state == "headers":

                headerMatch = self.headerParser.match(line)
                if headerMatch:
                    key = headerMatch.group(1)
                    value = headerMatch.group(2)

                    if key == "LENGTH":
                        length = int(value)
                    elif key == "TO":
                        to_ = value
                    else:
                        from_ = value
                    
                elif line == "":
                    # then we are done with headers!
                    if length == 0:
                        return SMS(to_, from_, body)
                    else:
                        state = "body";
                        bodyLinesRemaining = length
                
                else:
                    # then this was in invalid line for header mode
                    raise RuntimeError("Invalid line while parsing headers: %s" % line)
                
            elif state == "body":
                body += line + "\n"
                bodyLinesRemaining -= 1

                if bodyLinesRemaining == 0:
                    # then we have slurped up all the body that we need to
                    return SMS(to_, from_, body);
            
            else:
                raise RuntimeError("Invalid state in message parser: %s" % state)
    