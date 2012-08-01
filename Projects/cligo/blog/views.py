# Create your views here.
from django.http import HttpResponse
from blog.models import Team
from django.template import Context, loader
from django.shortcuts import render_to_response

def index(request):
    return render_to_response('blog/index.html',{})

def product(request):
    return render_to_response('blog/products.html')
   
def about(request):
    return render_to_response('blog/about.html')

def team(request):
    team_list = Team.objects.all()
    t = loader.get_template('blog/team.html')
    c = Context({
                 'team_list': team_list,
                 })
    return HttpResponse(t.render(c))