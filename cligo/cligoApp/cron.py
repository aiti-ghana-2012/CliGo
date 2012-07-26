from django_cron import cronScheduler, Job
from messagesender import messageSender

print "hi"

class sendmessage(Job):
    # this code should run every 1 min = 60s
    run_every = 5
    
    def job(self):
        # this cde will execute every 1 min
        print "HELLO THERE!"
        messageSender()
        ### send message

cronScheduler.register(sendmessage)

print "here"