from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, "index.html")


def home(request):
    return HttpResponse("HomePage!")


def about(request):
    if request.is_ajax():
        return HttpResponse('CIAOOOOOOO')
    return render(request, "about.html")
