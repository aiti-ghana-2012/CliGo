from web import WebSMSClient
from terminal import SMSTerminal
from android_connect import AndroidSMS
import logger

import os
import sys
import time

DJANGO_KEY = 'a0c963e748b0480f86833d48ace78533'
DJANGO_URL = 'http://localhost:8000/sms/'

ANDROID_PORT = 7800
ANDROID_HOST = 'localhost'

class root:
    DEVICE = 'root'
    
    
    
def connect(*pipes):  
    for i in range(len(pipes) - 1):        
        pipes[i].receive(pipes[i+1].send, source=pipes[i+1].DEVICE)
        
def connect2(*pipes):
    connect(*pipes)
    connect(*pipes[::-1])
    
def run(pipe_templates, connector):
    
    # creating the pipes
    pipes = []
    for pipe_template in pipe_templates:
        try:
            if isinstance(pipe_template, tuple):
                klass = pipe_template[0]
            
                if len(pipe_template) > 1:
                    args = pipe_template[1]
                else:
                    args = ()
            
                if len(pipe_template) > 2:
                    kwargs = pipe_template[2]
                else:
                    kwargs = {}
                
            else:
                klass = pipe_template
                args = ()
                kwargs = {}
        except Exception as e:
            logger.log_error(root, "Unable to extract initialization parameters from")
            logger.log_error(root, repr(pipe_template))
            logger.log_error(root, "Aborting start.")
            
        try:
            pipe = klass(*args, **kwargs)
        except Exception as e:
            logger.log_error(root, "Error initializing %s with args %s and kwargs %s"
                % (repr(klass), repr(args), repr(kwargs))
            )
            logger.log_error(root, repr(e))
            logger.log_error(root, "Aborting start and shutting down")
            cleanup_and_quit(*pipes)
        
        pipes.append(pipe)
    
    connector(*pipes)
    
    for pipe in pipes:
        try:
            pipe.start()
            logger.log(root, "started device %s" % pipe.DEVICE)
        except Exception as e:
            logger.log_error(root, "unable to start %s:" % pipe.DEVICE)
            logger.log_error(root, e.message)
            logger.log_error(root, "shutting down.")
            cleanup_and_quit(*pipes)
        


    try:
        while True:
            for pipe in pipes:
                pipe.join(.2)
                if not pipe.isAlive() and pipe.upstream:
                    logger.log_error(root, "%s has terminated - shutting down" % pipe.DEVICE)
                    cleanup_and_quit(*pipes)
    except KeyboardInterrupt:
        logger.log_error(root, "KeyboardInterrupt - shutting down")
        cleanup_and_quit(*pipes)
        
def cleanup_and_quit(*pipes):
    for pipe in pipes:
        try:
            pipe.cleanup()
        except Exception as e:
            logger.log_error(root, "Error while shutting %s - %s" % (pipe.DEVICE, e.message))
    
    logger.log_highlight(root, "bye")
    os._exit(0)


pipe_templates = {
    'terminal' : SMSTerminal,
    'django'   : (WebSMSClient, (DJANGO_URL, DJANGO_KEY)),
    'android'  : (AndroidSMS, (ANDROID_HOST, ANDROID_PORT)),
}

if __name__ == "__main__":
    
    def badargs():
        logger.log(root, "Bad Command Line Arguments! Try `python main.py help`")
        sys.exit(1)
        
    def print_help_and_exit():
        print """
Usage:
python main.py help
    - shows this message
python main.py terminal django
    - creates a 2-way SMS connection between your terminal and a django app
python main.py android terminal
    - creates a 2-way SMS connection between an android device and your terminal
python main.py android django
    - creates a 2-way SMS connection between an android device and a django app
"""
        sys.exit(1)
        
    
    start = 1
    connector = connect2
    
    if len(sys.argv) < 2:
        badargs()
    
         
    if sys.argv[1] == "help" or sys.argv[1] == "h":
        print_help_and_exit()
        
    if sys.argv[1] == "oneway":
        connector = connect
        if len(sys.argv) < 3:
            badargs()
        start = 2
        
    
    this_run_pipe_templates = [pipe_templates.get(k.lower()) for k in [sys.argv[i] for i in range(start,len(sys.argv))]]
    if not all(this_run_pipe_templates):
        badargs()
    
    run(this_run_pipe_templates, connector)
        
    
        
    
    
    
