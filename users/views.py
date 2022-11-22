from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from projects.models import Project
from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    context={'profiles':profiles}
    return render(request, 'users/profiles.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('projects')
    
    if request.method=='POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request, 'Username does not exist')
            
        user=authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'profiles')   #later send them to account
        else:
            messages.error(request, 'Username or password does not exist')
            
    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.error(request, 'User was logged out!')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form= CustomUserCreationForm()
    
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request, "Account created!")
            
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)