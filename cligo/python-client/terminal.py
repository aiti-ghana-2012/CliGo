"""
SMS sender emulator from terminal
"""

import threading
from SMS import SMS, SMSPipelineElement

import os
import logger

class SMSTerminal(SMSPipelineElement):
    
    
    def __init__(self):
        SMSPipelineElement.__init__(self, 'terminal', 'terminal')
        logger.log(self, "terminal SMS device initialized. exit by writing DO:QUIT after 'To:'")
    
    def send(self, sms):
        """
        prints the given SMS to STDOUT
        """
        logger.log_send(self, sms)
        print sms
                
        
    def listen(self):
        print "Enter Your SMS:"
        sms_dict = {}
        
        sms_dict['to_number'] = raw_input("To: ")
        sms_dict['from_number'] = raw_input("From: ")
        sms_dict['body'] = raw_input("Body:\n")
        
        
        if sms_dict['to_number'] == "DO:QUIT":
            return False
                    
        sms = SMS.from_dictionary(sms_dict)
        
        logger.log_receive(self, sms)
        self.receive_callback(sms)
            