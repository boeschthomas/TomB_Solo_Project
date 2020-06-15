from django.shortcuts import render, redirect
import bcrypt
from django.contrib import messages
from .models import *


def index(request):
    return render(request, 'index.html')

def register(request):
    print(request.POST)
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    hashed_password = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
    new_user = User.objects.create(first_name=request.POST['fname'], last_name=request.POST['lname'], email=request.POST['email'], password=hashed_password)
    print(new_user, "This is my new user!")
    request.session['name'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect('/home')

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if len(logged_user)>0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            print(logged_user, "logged user was signed in!")
            request.session['name'] = logged_user.first_name
            request.session['id'] = logged_user.id
            return redirect('/home')

    return redirect('/')

def home(request):
    if 'name' in request.session:
        return render(request, 'home.html')
    return redirect('/')

def my_page(request, id):
    context = {
        'user': User.objects.all()
    }
    return render(request, 'my_page.html', context)
   

def comm_page(request, id):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'all_users.html', context)

def create_page(request):
    return render(request, 'my_page.html')




# Create your views here.
