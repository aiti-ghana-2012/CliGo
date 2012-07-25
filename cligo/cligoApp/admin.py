from cligoApp.models import Hospital, Messages, Subscriber
from django.contrib import admin

class MessagesAdmin (admin.ModelAdmin):
    fieldsets = [
                 ('Details',               {'fields': ['message_type','message_week']}),         #modifying the view in the messages admin page
                 ('Message', {'fields': ['message']}),
                 # ('Other Information', {'fields': ['date_created'] , 'classes':['collapse']}),
                 ]
    
    list_display = ('message_type','date_created','message')                            #the fields to display in the admin listing page
    list_filter = ('message_type','message_week')                                       #the filter method on the right side
    search_fields = ['message']                                                         #where searches are made into
    
class SubscriberAdmin (admin.ModelAdmin):
    list_display = ('name_of_subcriber','registration_date','number_of_weeks','telephone_number')
    list_filter = ('number_of_weeks','registration_date')
    
    fieldsets = [
                 ('Subscriber Info', {'fields': ['name_of_subcriber','telephone_number','center_code','number_of_weeks'],
                                      'classes': ['collapse']})]

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name','region','center_code')
    list_filter = ('region',)
    
admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Messages,MessagesAdmin)
admin.site.register(Subscriber,SubscriberAdmin)