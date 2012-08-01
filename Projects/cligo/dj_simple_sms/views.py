# Create your views here.

from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import SMS, Device
from util import authorize, get_callable

import json

from django.conf import settings






@csrf_exempt
def sms(request):
    """
    Handles both the get and the post
    
    first thing is checks to make sure that the incoming message
    has the right secret device key
    
    POST:
    use the post data to create a SMS, and add it to the database
    will return empty 200 if success, or 500/400 with an {'error': <error message>} json body
    
    GET:
    gets up to max_sms sms, and returns them in a json list
    as well as a sms_count
    """   
    
    attrs = ('to_number','from_number','body')
    
    if request.method == "POST":
        
        device = authorize(request.POST.get('key'))
        if device is None:
            return HttpResponseForbidden()
        
        sms_dict = {}
        for attr in attrs:
            
            post_val = request.POST.get(attr)
            if post_val is None:
                return HttpResponseBadRequest("POST must have attribute %s" % attr)
            
            sms_dict[attr] = post_val
        
        new_sms = SMS(**sms_dict)
        
        sms_handlers = []
        sms_handler_tuple = getattr(settings,'SMS_HANDLERS',[])
        for sms_handler_string in sms_handler_tuple:
            sms_handlers.append(get_callable(sms_handler_string))
        
        # call the handlers? is this the best way?
        for sms_handler in sms_handlers:
            retval = sms_handler(new_sms)
            if retval is False:
                break
                
        return HttpResponse()
        
    elif request.method == "GET":
        """
        Remove this section if you will not be using
        The database as a queue for SMS sending-consumers
        """
        
        
        device = authorize(request.GET.get('key'))
        if device is None:
            return HttpResponseForbidden()
        
        max_sms = request.GET.get('max_sms',getattr(settings,'SMS_MAX_SMS_GET',10))
        
        # ok, get that many!
        if max_sms is None:
            sms_set = SMS.objects.all().order_by('datetime')
        else:
            sms_set = SMS.objects.all().order_by('datetime')[:max_sms]

            
        sms_list = list(sms_set.values(*attrs))
        
        count = len(sms_list)
        
        data_out = {'sms_count':count,'sms':sms_list}
        
        for sms in sms_set:
            sms.delete()
        
        return HttpResponse(json.dumps(data_out))
        
        

        
        
        