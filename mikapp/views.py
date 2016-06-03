from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hello World!")


def home(request):
    return HttpResponse("HomePage!")
