# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from views import addressGet


urlpatterns = patterns('',
    url(r'^(?P<zipcode>[\w-]+)/$', addressGet, name='address'),
)
