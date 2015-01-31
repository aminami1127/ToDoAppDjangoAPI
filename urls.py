# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'),     # 一覧
)

