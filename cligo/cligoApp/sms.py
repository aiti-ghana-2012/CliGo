'''
Created on Jul 25, 2012

@author: philip
'''

from dj_simple_sms import models
from cligoApp.models import Subscriber, Hospital

def handle_cligo_sms(sms):
    message = sms.from_number+ ', ' + sms.body
    message = [f.strip() for f in message.split(',')]
    
    if len(message) == 4:
        if Hospital.objects.get(center_code = message[2]):
            if Subscriber.objects.get(telephone_number = message[0]):
                print "user exists"
                notify = models.SMS(to_number=sms.from_number, from_number ='cligo', body="Welcome to cligo! You're already registered")
                notify.send()
            else:
                new_subscriber = Subscriber(
                                            telephone_number=message[0],
                                            name_of_subcriber=message[1],
                                            center_code=Hospital.objects.get(center_code = message[2]),
                                            number_of_weeks= int(message[3])
                                            )
                new_subscriber.save()
                print "user entered successfully"
                notify = models.SMS(to_number=sms.from_number, from_number ='cligo', body='Welcome to cligo! Your registration has been processed')
                notify.send()
        else:
            print "error"
            notify = models.SMS(to_number=sms.from_number, from_number ='cligo', body='From cligo! Please check your center code.')
            notify.send()
            
    else:
        print "failure"
        notify = models.SMS(to_number=sms.from_number, from_number ='cligo', body='From cligo! Please check your input for commas eg. Name, centercode, number_of_weeks(reg. Elvis, Kolebu, 5)')
        notify.send()
        
    #print "Cligo sms received, body: %s" % sms.body
    print "###########################################"
    #print "Were going to send one back!"
    
    