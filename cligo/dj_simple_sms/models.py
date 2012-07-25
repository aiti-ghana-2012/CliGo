from django.db import models

from django.contrib import admin

import uuid

class SMS(models.Model):
    
    to_number = models.CharField(max_length=64)
    from_number = models.CharField(max_length=64)
    body = models.CharField(max_length=160)
    
    datetime = models.DateTimeField(auto_now_add=True)

    def send(self):
        """
        Change this to use another method or api for sending an SMS
        """
        self.save()
        
        
    def to_message(self):
        return "To: %s\nFrom: %s\nBody:\n%s" % (self.to_number, self.from_number, self.body)
    
    
class Device(models.Model):
    
    name = models.CharField(max_length=64)
    
    def generate_key():  
        return uuid.uuid4().hex
    key = models.CharField(max_length=32,default=generate_key,db_index=True,editable=False)
    

class SMSAdmin(admin.ModelAdmin):
    list_display = ('to_number','from_number','body')
    ordering = ('datetime',)
    
class DeviceAdmin(admin.ModelAdmin):
    
    list_display= ('name','key')
    
    
admin.site.register(SMS, SMSAdmin)
admin.site.register(Device, DeviceAdmin)