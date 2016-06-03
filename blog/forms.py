#coding=utf-8
# Author: MikeWil
# Date: 03/06/16
# Filename: forms.py

from django import forms

from .models import Post


class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ('title', 'text', )