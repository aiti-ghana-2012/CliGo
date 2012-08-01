'''
Created on Jul 25, 2012

@author: philip
'''

from dj_simple_sms import models
from cligoApp.models import Subscriber, Hospital
from getDay import getDay

def handle_cligo_sms(sms):    
    message = sms.from_number+ ', ' + sms.body.lower()
    message = [f.strip() for f in message.split(',')]
    try:
        if len(message) == 4:
            if Hospital.objects.get(center_code = message[2]):
                if Subscriber.objects.filter(telephone_number = message[0]) : 
                    print "user exists"
                    notify = models.SMS(to_number=  sms.from_number, from_number ='CliGo', body="Welcome to CliGo! You're already registered in the system")
                    notify.send()
                else:
                    new_subscriber = Subscriber(
                                                telephone_number=message[0],
                                                name_of_subcriber=message[1],
                                                center_code=Hospital.objects.get(center_code = message[2]),
                                                number_of_weeks= int(message[3]),
                                                day = getDay().get_day()
                                                )
                    new_subscriber.save()
                    print "user entered successfully"
                    notify = models.SMS(to_number=sms.from_number, from_number ='CliGo', body='Welcome to CliGo! Your registration has been processed')
                    notify.send()
            else:
                print "error"
                notify = models.SMS(to_number=sms.from_number, from_number ='CliGo', body='From CliGo! Please check your center code.')
                notify.send()
                
        else:
            print "failure"
            notify = models.SMS(to_number=sms.from_number, from_number ='CliGo', body='From CliGo! Please check your input for commas eg. Name, centercode, number_of_weeks(eg. Elvis, Kolebu, 5)')
            notify.send()
        
    except:
        print "One user entered a bad info."
        notify = models.SMS(to_number=sms.from_number, from_number ='CliGo', body='From CliGo! Please check your Hospital code')
        notify.send()
    
    
    