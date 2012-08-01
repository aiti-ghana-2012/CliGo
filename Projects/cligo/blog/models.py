from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length = 50)
    institution = models.CharField(max_length = 200, blank=True)
    brief_description = models.TextField()
    #position = models.TextField(max_length = 100)
    #specialty = models.TextField(max_length = 100)
    full_profile = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.name