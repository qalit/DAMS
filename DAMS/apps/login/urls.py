from django.conf.urls import patterns, include, url
from DAMS.apps.login.views import *
 
urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    url(r'^daftar/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home)
    )