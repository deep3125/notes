from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from json import dumps
# Create your views here.

def login_page(request):
    return render(request, 'accounts/login.html')

def register_page(request):
    return render(request, 'accounts/register.html')

def register_user(request):
    user_name = request.POST.get('user_name')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')   
    try:
        User.objects.get(username=user_name)
        messages.error(request, 'Username already taken')
        return redirect('/accounts/register/')

    except:
        if password1==password2:
            user = User.objects.create_user(password=password1, username=user_name, email=email,first_name=first_name, last_name=last_name)
            return redirect('/')
        else:
            messages.error(request, 'Passwords must match')
            return redirect('/accounts/register/')

def Logout(request):
    logout(request)
    return redirect('/')
    
def log_user_in(request):
    user_name = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=user_name, password=password)
    if user is not None:
        login(request, user)
        return redirect('/')
    else:
        try:
            User.objects.get(username=user_name)
            messages.error(request, 'Wrong password')
            return redirect('/accounts/login/')
        except:
            messages.error(request, 'This User doesn\'t exists' )
            return redirect('/accounts/login')