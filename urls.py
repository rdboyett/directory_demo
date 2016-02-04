# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from .views import DirectoryListView, DirectoryDetailView, DirectoryCreateView, DirectoryUpdateView, DirectoryDeleteView

urlpatterns = [
    url(r'^$', DirectoryListView.as_view(), name="list"),
    url(r'^(?P<pk>(\d+))/$', DirectoryDetailView.as_view(), name='detail'),
    url(r'^create/$', DirectoryCreateView.as_view(), name="create"), #ajax
    url(r'^update/(?P<pk>(\d+))/$', DirectoryUpdateView.as_view(), name="update"),
    url(r'^delete/(?P<pk>(\d+))/$', DirectoryDeleteView.as_view(), name="delete"),
]
