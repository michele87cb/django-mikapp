#coding=utf-8
# Author: MikeWil
# Date: 03/06/16
# Filename: urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]