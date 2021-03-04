from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from Doodle_App.models import *

def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request, 'registration.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def admin(request):
    return render(request, 'admin.html')

def profile(request):
    return render(request, 'profile.html')

def edit_profile(request):
    return render(request, 'edit_user.html')

def admin_edit(request):
    return render(request, 'admin_edit.html')