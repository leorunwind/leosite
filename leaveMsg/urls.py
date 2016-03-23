from django.conf.urls import *
from leaveMsg.view import archive

urlpatterns = patterns('',
                      url(r'^$',archive),
                      )