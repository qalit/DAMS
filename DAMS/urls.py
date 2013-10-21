from django.conf.urls import patterns, include, url
from django.contrib import admin

#from apps.about.views import about, current_time
from DAMS.apps.polls.views import *

# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', include('DAMS.apps.home.urls')),
    # url(r'^DAMS/', include('DAMS.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include('admin.site.urls')),
    #url(r'^polls/$', Poll),
    url(r'^about/$', include('DAMS.apps.about.urls')),
    url(r'^about/$', include('DAMS.apps.about.urls')),
    #url(r'^about/time/$', current_time),
    #url(r'^polls/', include('polls.urls')),
)
