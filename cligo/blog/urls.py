from django.conf.urls import patterns, url

urlpatterns = patterns('blog.views',
    url(r'^$','index', name='index'),
    url(r'^product/','product', name='product'),
    url(r'^about/$', 'about', name='about'),
    url(r'^team/$','team', name='team'),
)
