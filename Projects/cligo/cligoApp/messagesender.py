from cligoApp.models import Subscriber, Messages
from cligoApp.getDay import getDay
from dj_simple_sms import models
from datetime import date

def messageSender():
    #Check if subscriber day matches with the current day
    today = getDay().get_day()
    subscriber_days = Subscriber.objects.filter(day = today)
    message_week = Messages.objects.all()
    
    #getting the messages that need to be sent to specific users
    for message in message_week:
        for subscriber in subscriber_days:
            sbday = subscriber.number_of_weeks
            add_days = str(date(2012,8,10) - subscriber.registration_date)                  #this is to convert the datetime format into str
            #print "days: %s" , add_days
            if (int(add_days.split(' ')[0]) % 7) == 0:
                sbday = sbday + int(add_days.split(' ')[0]) / 7
                
            if message.message_week == sbday:
                if subscriber.message.filter(id=message.id):
                    #print "no message to send to: %s" %str(subscriber.telephone_number)
                    pass
                else:
                    #call function to send message to number
                    notify = models.SMS(to_number=subscriber.telephone_number, from_number ='cligo', body=message.message)
                    
                    subscriber.message.add(message)
                    
                    notify.send()
                    print "message sent to number: %s" %str(subscriber.telephone_number)
    
    