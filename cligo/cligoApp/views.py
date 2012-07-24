# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response

def CligoHomePage(request):
    
    return HttpResponse("This is <b>Cligo</b> Homepage enjoy yourself")

def about(request):
    
    return HttpResponse("This is the <b>about</b> page ")

def contact(request):
    
    return HttpResponse("This is our <b>contact</b> page")