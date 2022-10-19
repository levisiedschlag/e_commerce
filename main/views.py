from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.

def front_page(request:HttpRequest):
    return render(request, 'main/frontpage.html', {'dados':'Hello friend'})

def about_page(request:HttpRequest):
    return render(request, 'main/aboutpage.html', {'dados':'Hello friend'})