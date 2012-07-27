from django_cron import cronScheduler, Job
from messagesender import messageSender

print "Hello This is Cligo Cron"

class sendmessage(Job):
    # this code should run every 1 min = 60s
    run_every = 1
    
    def job(self):
        # this cde will execute every 1 min
        print "Job processing ... ..."
        messageSender()
        ### send message


cronScheduler.register(sendmessage)