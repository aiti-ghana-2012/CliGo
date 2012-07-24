from django.db import models

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
    center_code = models.IntegerField()
    contact_number = models.CharField(max_length = 10)
    region = models.CharField(max_length = 20, choices=REGION_LIST)
    location = models.CharField(max_length = 50)
    
    def __unicode__(self):
        return self.name

class Messages(models.Model):
    message = models.CharField(max_length = 160)
    message_type = models.CharField(max_length = 50)
    message_week = models.IntegerField()
    
    def __unicode__(self):
        return self.message
    
class Subscriber (models.Model):
    number_of_weeks = models.IntegerField()
    name_of_subcriber = models.CharField(max_length = 50)
    telephone_number = models.CharField(max_length = 10)
    
    #Foreign keys
    message = models.ForeignKey(Messages)
    center_code = models.ForeignKey(Hospital)
    
    def __unicode__(self):
        return self.name_of_subcriber
