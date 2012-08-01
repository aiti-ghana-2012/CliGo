import requests
import sys

import threading
import time
import collections

import logger

from SMS import SMS, SMSPipelineElement

DEBUG = True
VERBOSE = False

class WebSMSClient(SMSPipelineElement):
        
    MAX_SMS = 10
    POLL_TIMEOUT = 5
    
    def __init__(self, url, key):
        SMSPipelineElement.__init__(self, 'django connector', 'django')
        threading.Thread.__init__(self)
        
        self.url = url
        self.key = key        
        logger.log(self, "created with device key %s and url %s" % (key, url))
        
        self.sms_queue = collections.deque()
            
    def send(self, sms):
     
        data_dict = {
            'to_number' : sms.to_number,
            'from_number' : sms.from_number,
            'body' : sms.body,
            'key' : self.key
        }
        
        result = requests.post(self.url, data=data_dict)
        if not result.status_code == requests.codes.ok:    
            logger.log_error(self, "error %d - %s posting sms to %s" %
                (result.status_code, result.error, self.url))               
            log_response(result)           
            return False        
        else:
            logger.log_send(self, sms)
            return True
            
    def fill_queue(self):
        """
        will fill the queue back up to however many it can
        will only try once
        """
        
        desired_sms = self.MAX_SMS - len(self.sms_queue)    
        data_dict = {
            'max_sms' : desired_sms,
            'key' : self.key
        }
        
        result = requests.get(self.url, params=data_dict)        
        if not result.status_code == requests.codes.ok:
            logger.log_error(self, "error filling queue: %d - %s" % (result.status_code, result.error))
            log_response(result)
            return 0
        
        count = result.json['sms_count']
        
        for sms in result.json['sms']:
            new_sms = SMS.from_dictionary(sms)
            self.sms_queue.append(new_sms)
        
        if VERBOSE:
            logger.log(self, "grabbed %s messages from django queue" % count)
        
        return len(self.sms_queue)
        
    def listen(self):
        sms_count = len(self.sms_queue)
        
        # if i'm out of things, i need to get some more!
        if sms_count == 0:
            sms_count = self.fill_queue()
        
        # but if it is _still_ 0... 
        if sms_count == 0:
            time.sleep(self.POLL_TIMEOUT)
        
        else:
            received_sms = self.sms_queue.popleft()
            logger.log_receive(self, received_sms)
            self.receive_callback(received_sms)

            time.sleep(.1)
                    
                
        
def log_response(response):
    if DEBUG:
        out_file = open('errresponse.html', 'w')
        out_file.write(response.content)
        out_file.close()
        

    