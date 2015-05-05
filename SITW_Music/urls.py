from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from myplaylists.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SITW_Music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^logout/$', log_out),
    url(r'^login/$', 'django.contrib.auth.views.login'),

    url('^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/')),

    url(r'^$', mainpage, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myplaylists/', include('myplaylists.urls', namespace='myplaylists')),
)
