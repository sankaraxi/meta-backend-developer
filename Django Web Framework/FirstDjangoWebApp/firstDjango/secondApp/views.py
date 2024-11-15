from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    content = "Welcome to the secondApp homepage!"
    return HttpResponse(content)