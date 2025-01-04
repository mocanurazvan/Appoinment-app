from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import Programare


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')  # Redă template-ul about.html


def cursuri(request):
    return render(request, 'cursuri.html')  # Redă template-ul programari.html


def dashboard(request):
    return render(request, 'dashboard.html')  # Redă template-ul dashboard.html


def disponibilitate(request):
    return render(request, 'disponibilitate.html')  # Redă template-ul dashboard.html


