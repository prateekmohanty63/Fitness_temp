from django.shortcuts import render
from .models import Events

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def Event(request):
    return render(request,'Event.html')