# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'), #show all or create new
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'), #retrieve, update, delete
)

