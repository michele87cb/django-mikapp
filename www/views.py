from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")


def home(request):
    return HttpResponse("HomePage!")


def about(request):
    return render(request, "about.html")
