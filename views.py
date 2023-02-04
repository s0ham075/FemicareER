from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return render(response,"main/homepage.html",{})
   
# Create your views here.
