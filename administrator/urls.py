#coding=utf-8
# Author: MikeWil
# Date: 03/06/16
# Filename: urls.py

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
]