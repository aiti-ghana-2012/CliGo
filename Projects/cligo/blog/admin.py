from blog.models import Team
from django.contrib import admin

class TeamAdmin(admin.ModelAdmin):
    fieldsets = [
              ("Basic Info",   {'fields': ['name','brief_description']}),
              ('Details',       {'fields': ['institution','full_profile'],
                                    'classes': ['collapse']})
            ]
    
admin.site.register(Team, TeamAdmin)