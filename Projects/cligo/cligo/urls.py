from django.conf.urls import patterns, include, url
#cron addtition
import django_cron
django_cron.autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cligo.views.home', name='home'),
    # url(r'^cligo/', include('cligo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cligo/', include('cligoApp.urls')),
    url(r'^sms/', include('dj_simple_sms.urls')),
    url(r'^afiday/', include('blog.urls')),
    
)
