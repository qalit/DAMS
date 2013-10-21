from django.conf.urls.defaults import *
 
urlpatterns = patterns('',
                       (r'^$', 'DAMS.apps.home.views.index'),
                        
                       )