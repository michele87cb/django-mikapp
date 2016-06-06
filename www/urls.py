# coding=utf-8
# ---------------------------------------------------------------
# Project: djangomik
# Date   : 03/06/2016 10:44
# Author : MikeWil
# Source : urls.py
# ---------------------------------------------------------------
# MICHELE GUGLIELMI
# ---------------------------------------------------------------

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'home/', views.home, name='home'),
    url(r'about/', views.about, name='about')
]