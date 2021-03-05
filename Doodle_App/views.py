from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from Doodle_App.models import User, Blog, Comment
from django.contrib import messages
import re
import bcrypt

def index(request):
    return render(request,'index.html')

def registration(request):
    return render(request, 'registration.html')

def register(request):
    errors = User.objects.registrationValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/registration')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName'],
            email=request.POST['email'],
            password=pw_hash,
            )
        request.session['userID'] = user.id
        request.session['user_level'] = user.user_level
        return redirect('/dashboard')

def dashboard(request):
    if 'userID' in request.session:
        user = User.objects.get(id=request.session['userID'])
        context = {
            "user": user,
            "users" : User.objects.all(),
            "blogs" : Blog.objects.all(),
            "comments" : Comment.objects.all(),
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/')

def admin(request):
    if request.session['user_level'] == 1:
        user = User.objects.get(id=request.session['userID'])
        context = {
            "user": user,
            "users" : User.objects.all(),
            "blogs" : Blog.objects.all(),
        }
        return render(request, 'admin.html', context)
    else:
        return redirect('/dashboard')

def profile(request,num):
    user = User.objects.get(id=num)
    if 'userID' in request.session and request.session['userID'] == user[id]:
        context = {
            'user': user,
        }
        return render(request, 'profile.html',context)
    else:
        return redirect('/dashboard')

def edit_profile(request):
    return render(request, 'edit_user.html')

def admin_edit(request):
    return render(request, 'admin_edit.html')

def login(request):
    errors = User.objects.loginValidator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        user = User.objects.filter(email=request.POST['email'])
        if not user:
            messages.error(request, "User doesn't exist under that email, please register")
            return redirect('/')
        else:
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                request.session['userID'] = user[0].id
                request.session['user_level'] = user[0].user_level
                return redirect('/dashboard')
            else:
                messages.error(request, "Invalid login credentials, please try again.")
                return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')