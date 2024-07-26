from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return render(request, "index.html")

def home(request):
    return HttpResponse("Home page")

def contact(request):
    return HttpResponse("fuck you")