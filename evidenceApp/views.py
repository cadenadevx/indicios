from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'auth/login.html')

def register(request):
    return render(request, 'auth/register.html', {
        'form': UserCreationForm
    })

def close(request):
    return render(request, 'auth/close.html')

def profile(request):
    return render(request, 'auth/profile.html')

def createCad(request):
    return render(request, 'crud/createCad.html')

def editCad(request):
    return render(request, 'crud/editCad.html')

def deleteCad(request):
    return render(request, 'crud/deleteCad.html')

def updateCad(request):
    return render(request, 'crud/updateCad.html')

