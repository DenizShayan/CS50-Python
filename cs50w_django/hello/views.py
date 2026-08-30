from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def deniz(request):
    return HttpResponse("Hello, Deniz!")

def david(request):
    return HttpResponse("Hello, David!")