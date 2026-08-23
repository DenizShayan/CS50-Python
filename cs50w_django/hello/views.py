from django.shortcuts import render

# Create your views here.
def index(requst):
    return HttpResponse("Hello, world!")