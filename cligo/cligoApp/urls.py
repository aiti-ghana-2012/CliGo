from django.conf.urls import patterns, url

urlpatterns = patterns('cligoApp.views',
    url(r'^$', 'CligoHomePage', name='index'),
    url(r'^about/$', 'about', name='about'),
    url(r'^contact/$', 'contact', name='about'),
    
)
