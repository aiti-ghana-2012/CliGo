from termstyle import termstyle
import datetime

color_order = [
    'blue',
    'green',
    'cyan',
    'yellow',
]


device_stylehash = {
    'root' : termstyle.magenta,
}


def timestamp():
    return datetime.datetime.today().strftime("%m-%d-%Y %H:%M:%S")
    
def get_device_style(device):
    global color_order # :(
    
    if device.DEVICE in device_stylehash:
        style = device_stylehash[device.DEVICE]
        
    else:
        if color_order:
            new_color = color_order[0]
            color_order = color_order[1:]
        else:
            raise RuntimeError("Out of colors!")
        
        style = getattr(termstyle, new_color)
        device_stylehash[device.DEVICE] = style
        
    return style
    
def get_source(device):
    source = getattr(device, 'source')
    return 'from %s' % source if source else ''
    

    

def log(device, message):
    style = get_device_style(device)        
    print "[%s] - [%s]: %s" % (timestamp(), style(device.DEVICE), message)
    
    
def log_send(device, sms):
    message = "Sent %s %s to %s" % (repr(sms), get_source(device), device.sink)
    log(device, message)
    
def log_receive(device, sms):
    message = "Received %s from %s" % (repr(sms), device.sink)
    log(device, message)
    
def log_error(device, message):
    message = "!! -- %s" % message
    message = termstyle.red.bold(message)
    log(device, message)
    
def log_highlight(device, message):
    message = termstyle.underlined.cyan.bold(message)
    log(device, message)