from django.http import HttpResponse


def hello(request):
    return HttpResponse("Hello, Docker + Django + Python 3.14!")
