from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.contrib import messages
from .forms  import ProjectForm, ReviewForm
from .models import Project, Tag, Review
from .utils import searchProject
from django.contrib.auth.decorators import login_required

# Create your views here.


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

def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request, "projects/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context={'form':form}
    return render(request, "projects/project_form.html", context)

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'object':project}
    return render(request, 'projects/delete.html', context)