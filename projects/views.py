from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from .forms  import ProjectForm, ReviewForm
from .models import Project, Tag, Review
from .utils import searchProject
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.?search_query=tola


def projects(request):
    
    projects, search_query = searchProject(request)

    
    context={'projects':projects, 'search_query':search_query}
    return render(request, 'projects/projects.html', context)



def project(request, pk):
    project = Project.objects.get(id=pk)
    tags = project.tags.all()
    reviews = project.review_set.all()
    form = ReviewForm()
    
    if request.method == 'POST':
        form=ReviewForm(request.POST)
        review = form.save(commit=False)  #commit=False to get instance of that review
        review.project= project
        review.owner = request.user.profile
        review.save()
        
        project.getVoteCount
        messages.success(request, 'Your review was successfully submitted!')
        
        return redirect('project', pk=project.id)
    
    
    context={'project':project, 'tags':tags, 'reviews':reviews, 'form':form}
    return render(request, 'projects/single_project.html', context)


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            proj = form.save(commit=False)
            proj.owner = profile
            
            proj.save()
            
            # checking if tag written by user is created and then adding into database
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                proj.tags.add(tag)
                
                
                
            return redirect('account')
              

        
    context={'form':form} 
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
             
            # checking if tag written by user is created and then adding into database
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
                # project.tags.lower()
            return redirect('account')
        
    context={'form':form}
    if profile != project.owner:
        return HttpResponseRedirect('handler404')
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('account')
    context={'object':project}
    return render(request, 'projects/delete.html', context)











############################
# 404 VIEW
############################

def page_not_found(request, exception):
    return render(request, '404.html', status=404)