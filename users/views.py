from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, MessageForm, ProfileForm, SkillForm
from projects.models import Project
from .models import Profile, Message
from .utils import searchProfile
import requests
import json
# Create your views here.



def profiles(request):
    profiles, search_query = searchProfile(request)
    
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
        
    # geolocation_json = get_ip_geolocation_data(ip)

    # geolocation_data = json.loads(geolocation_json)

    # country = geolocation_data['country']


    # region = geolocation_data['region']
    
    context={'profiles':profiles, 'search_query':search_query}
    return render(request, 'users/profiles.html', context)


def work_with_us(request):
    return render(request, 'users/work_with_us.html')

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
    context={'profile':profile, 'projects':projects, 'skills':skills}
    return render(request, 'users/user_profile.html', context)






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
            user = form.save()
            # user.username = user.username.lower()
            # user.email=profile.email
            # user.save()
            
            messages.success(request, "Account created!")
            
            login(request, user)
            return redirect('edit-profile')
        else:
            messages.error(request, "Error occurred during registration")
    context={'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)


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



@login_required(login_url='login')
def account(request):
    profile=request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context={'profile':profile, 'skills':skills, 'projects':projects}
    return render(request, 'users/account.html', context)

# -------------------------- #

#    Skill crud

# -------------------------- #
@login_required(login_url='login')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm(request.POST)
    if request.method=='POST':
        form=SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "You have successfully added skill.")
            return redirect('account')

        else:
            messages.error(request, "Error occurred")
    context={'form':form}
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('account')
    context={'form':form}
    if profile != skill.owner:
        return HttpResponseRedirect('handler404')
    return render(request, 'users/skill_form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method=='POST':
        skill.delete()
        return redirect('account')
    context={'object':skill}
    if profile != skill.owner:
        return HttpResponseRedirect('handler404')
    return render(request, 'users/delete.html', context)

# -------------------------- #

#    End of Skill crud

# -------------------------- #



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
    # if request.user.profile == recipient:
    #     return HttpResponseRedirect("handler404")
    return render(request, 'users/message_form.html', context) 

 