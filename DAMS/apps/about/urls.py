from django.conf.urls.defaults import *
 
urlpatterns = patterns('',
                       (r'^$', 'DAMS.apps.about.views.about'),
                       (r'^$', 'DAMS.apps.about.views.current_time'),
                        
                       )