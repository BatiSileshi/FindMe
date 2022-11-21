from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q

from .forms  import ProjectForm
from .models import Project, Tag, Review
from .utils import searchProject

# Create your views here.


def projects(request):
    
    projects, search_query = searchProject(request)

    
    context={'projects':projects, 'search_query':search_query}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    reviews = project.review_set.all()
    tags = project.tags.all()
    context={'project':project, 'tags':tags, 'reviews':reviews}
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