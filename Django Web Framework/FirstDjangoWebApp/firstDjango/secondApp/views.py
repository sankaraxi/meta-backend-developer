from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    content = "Welcome to the secondApp homepage!"
    return HttpResponse(content)

def django(request):
    return HttpResponse("<html><body><h1 style='color:blue'>Welcome to the Django homepage!</h1></body></html>")