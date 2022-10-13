from django.shortcuts import render
from django.contrib import messages, auth
from django.shortcuts import render, redirect
from .models import Account
from django.contrib.auth import authenticate
6
# Create your views here.

def Home(request):
    return render(request,"index.html")


def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are logged in')
            # store user details in session
            request.session['email']=email
            return redirect('home')
        else:
            messages.error(request, 'invalid login credentials')
            return redirect('register')
    return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        fname=request.POST['fname']
        lname=request.POST['lname']
        phone_number=request.POST['tel']
        print(email,password,fname,lname,phone_number)
        if Account.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('register')
        else:
            user=Account.objects.create_user(email=email, password=password, fname=fname, lname=lname,  phone_number=phone_number)
            user.save()
            messages.success(request, 'you are registered')
            return redirect('/login')
    return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
