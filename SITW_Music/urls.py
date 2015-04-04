from django.conf.urls import patterns, include, url

from django.contrib import admin
from myplaylists.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SITW_Music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^logout/$', log_out),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myplaylists/', include('myplaylists.urls', namespace='myplaylists')),
)
