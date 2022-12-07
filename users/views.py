from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, MessageForm, ProfileForm
from projects.models import Project
from .models import Profile, Message
# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    
    context={'profiles':profiles}
    return render(request, 'users/profiles.html', context)


@login_required(login_url='login')
def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
    context={'profile':profile, 'projects':projects, 'skills':skills}
    return render(request, 'users/user_profile.html', context)



@login_required(login_url='login')
def editProfile(request):
    profile  = request.user.profile

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'You have successfully updated your profile')
            return redirect('account')
        else:
            messages.error(request,'There is an error while processing your in put')
    context = {'form':form}
    return render(request, 'users/profile_form.html',context)






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
            return redirect('edit-profile')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)


@login_required(login_url='login')
def account(request):
    profile=request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context={'profile':profile, 'skills':skills, 'projects':projects}
    return render(request, 'users/account.html', context)



@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    context={'messageRequests':messageRequests, 'unreadCount':unreadCount}
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context={'message':message}
    return render(request, 'users/message.html', context)

@login_required(login_url='login')
def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    
    try:
        sender = request.user.profile
    except:
        sender = None
        
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit = False)
            message.sender = sender
            message.recipient = recipient
            
            if sender:
                message.name = sender.name
                message.email = sender.email
            
            message.save()
            
            messages.success(request, 'Your message was successfully sent')
            return redirect('user-profile', pk=recipient.id)
    
    context={'recipient':recipient, 'form':form}
    return render(request, 'users/message_form.html', context) 