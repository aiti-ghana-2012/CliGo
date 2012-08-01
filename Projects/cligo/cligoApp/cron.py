from django_cron import cronScheduler, Job
from messagesender import messageSender

print "Hello This is Cligo Cron"

class sendmessage(Job):
    # this code should run every 1 min = 60s
    run_every = 10
    
    def job(self):
        # this cde will execute every 5 min
        messageSender()
        ### send message

cronScheduler.register(sendmessage)