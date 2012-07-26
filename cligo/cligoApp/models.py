from django.db import models
#from datetime import date              #to get the time 

# Create your models here.
'''
// document written on Tue Jul 24, 2012 11:09:40AM

Hospital
Name String
CenterCode numeric
Contact number String
Location
string


Subscriber
Number_of_weeks Numeric
Name String
Telephone_number Numeric
FK: message_id
FK: CenterCode
Numeric


Messages
message String
Message_type String
Message_week numeric

'''

class Hospital (models.Model):
    REGION_LIST= (
                    ('gt accra','Greater Accra'),
                    ('ashanti','Ashanti'),
                    ('eastern','Eastern'),
                    ('western','Western'),
                    ('central','Central'),
                    ('northern','Northern'),
                    ('upEast','Upper East'),
                    ('upWest','Upper West'),
                    ('volta','Volta Region'),
                    ('brong','Brong Ahafo')
                    )
    name = models.CharField(max_length = 100)
    center_code = models.CharField(max_length = 10)
    contact_number = models.CharField(max_length = 10)
    region = models.CharField(max_length = 20, choices=REGION_LIST)
    location = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name

class Messages(models.Model):
    TYPES_LIST = (
                  ('tips','Health Tip'),
                  ('app','Appointment'),
                  ('gen','General Information')
                  )
    message_type = models.CharField(max_length = 50,choices=TYPES_LIST)
    message = models.TextField(max_length = 160)
    message_week = models.IntegerField()
    
    date_created = models.DateField(auto_now = True)
    
    def __unicode__(self):
        return self.message
    
class Subscriber (models.Model):
    number_of_weeks = models.IntegerField()
    name_of_subcriber = models.CharField(max_length = 50)
    telephone_number = models.CharField(max_length = 10)
    registration_date = models.DateField(auto_now = True)
    day = models.CharField(max_length = 10)
    
    message = models.ManyToManyField(Messages)                  #many to many relation for message and subscriber
    center_code = models.ForeignKey(Hospital)
    
    def __unicode__(self):
        return self.name_of_subcriber
    
    '''
    def register_subscriber(self, sms_from_number, sms_body):
        message = sms_from_number+ ', ' + sms_body
        message = [f.strip() for f in message.split(',')]
        
        if len(message) == 4:
            if Hospital.objects.get(center_code = message[2]):
                if Subscriber.objects.filter(telephone_number = message[0]) : 
                    print "user exists"
                    return "Exists"
                else:
                    new_subscriber = Subscriber(
                                                telephone_number=message[0],
                                                name_of_subcriber=message[1],
                                                center_code=Hospital.objects.get(center_code = message[2]),
                                                number_of_weeks= int(message[3])
                                                )
                    new_subscriber.save()
                    print "user entered successfully"
                    return "Successful"
            else:
                print "Center Error"
                return "Center Error"          
        else:
            print "Message Error"
            return "Message Error"
        '''
