#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework.views import APIView
try:
    from django.conf.urls import patterns
except ImportError:
    try:
        from django.conf.urls.defaults import patterns
    except ImportError:
        from django.urls import path
        patterns = lambda x: [path('', APIView.as_view())]


urlpatterns = patterns('', )
