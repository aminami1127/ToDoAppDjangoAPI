# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from todo import views

urlpatterns = patterns('',
                       # index.html
                       url(r'^$', views.index, name='index'),
                       # show all or create new
                       url(r'^list$', views.list, name='list'),
                       # retrieve, update, delete
                       url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
                       )
