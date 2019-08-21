from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,'home.html')

def about(request):
    return render(request,'dj1.html')

def contact(request):
    return render(request,'dj2.html')

def services(request):
    return render(request,'dj.html')