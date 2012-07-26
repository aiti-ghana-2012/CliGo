from cligoApp.models import Subscriber, Messages
from cligoApp.getDay import getDay
from dj_simple_sms import models

def messageSender():
    #Check if subscriber day matches with the current day
    today = getDay().get_day()
    subscriber_days = Subscriber.objects.filter(day = today)
    message_week = Messages.objects.all()
    
    #getting the messages that need to be sent to specific users
    for message in message_week:
        for subscriber in subscriber_days:
            if message.message_week == subscriber.number_of_weeks:
                #call function to send message to number
                notify = models.SMS(to_number=subscriber.telephone_number, from_number ='cligo', body=message.message)
                notify.send()
                print "send message to number"
        
    
    
sub = Subscriber.objects.all()

print "subscriber"