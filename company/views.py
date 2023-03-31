from django.shortcuts import render, redirect
from .forms import CompanyForm, JobPostForm
from .models import Invitation, JobPost, JobApplication
from django.http import HttpResponseRedirect, HttpResponse, Http404
from system_admin.models import CompanyAdmin
from django.contrib import messages
from users.utils import searchProfile
from users.models import Profile, Message
from django.contrib.auth.decorators import login_required

# Create your views here.
def register_company(request):
    profile = request.user.profile
    form = CompanyForm(request.POST) 
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully register your company.")
            return redirect('welcome-company')

        else:
            messages.error(request, "Error occurred")
    context={'form':form}
    if profile.looking_for == 'work':
        return HttpResponseRedirect('handler404')
    return render(request, 'company/form.html', context)



def welcome_company(request):

    context={}
    
    return render(request, 'company/welcome_company.html', context)


def company_home(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    
    context={'company':company}
    if profile != company_admin.admin:
        return HttpResponseRedirect('handler404')
    return render(request, 'company/company_home.html', context)


def invitations(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    admin=company_admin.admin
    
    invitations = Message.objects.filter(sender=admin)
    
    context={'company':company, 'invitations':invitations}
    if profile != company_admin.admin:
        return HttpResponseRedirect('handler404')
    return render(request, 'company/invitations.html', context)
  
      
@login_required(login_url="login")  
def jobs(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    
    admin=company_admin.admin
    
    jobs = JobPost.objects.filter(company=company)
    context={'jobs':jobs}
    
    return render(request, 'company/jobs.html', context)  
    
@login_required(login_url="login")  
def post_job(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    admin=company_admin.admin
    
    form = JobPostForm(request.POST)
    if request.method == 'POST':
        form=JobPostForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.company = company
            job.save()
            messages.success(request, "You have successfully posted a job.")
            return redirect('jobs')

        else:
            messages.error(request, "Error occurred")
    context = {'form':form}
    if profile != admin:
        return HttpResponseRedirect("handler404")
    return render(request, 'company/post_form.html', context)
      
     
@login_required(login_url="login")  
def update_job_post(request, pk):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    admin=company_admin.admin
    try:
        job = JobPost.objects.get(id=pk, company=company)  
    except:
        return HttpResponseRedirect('handler404')
    
    form = JobPostForm(instance=job)
    if request.method == 'POST':
      
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully updated a job.")
            return redirect('jobs')
        else:
            messages.error(request, "Error occurred, while updating. Please try again later")
    context={'form':form}  
    return render(request, 'company/post_form.html', context)


@login_required(login_url="login") 
def job_applications(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)

    company = company_admin.company
    job_apps = JobApplication.objects.filter(job__company=company)
    print(job_apps)
    context ={'job_apps': job_apps}

    return render(request, 'company/job_applications.html', context)

@login_required(login_url="login") 
def view_applicant(request, pk):
    profile = Profile.objects.get(id=pk)
    projects = profile.project_set.all()
    skills = profile.skill_set.all()
    context={'profile':profile, 'projects':projects, 'skills':skills}
    return render(request, 'company/applicant_profile.html', context)

# def invite(request):
#     profile = request.user.profile
#     company_admin = CompanyAdmin.objects.get(admin=profile)
#     admin = company_admin.admin
    
#     profiles, search_query = searchProfile(request)
    
#     context={'profiles':profiles, 'search_query':search_query, 'admin':admin}
#     return render(request, 'users/profiles.html', context)


# def invite_final(request, id):
#     employee = Profile.objects.get(id=id)
    
#     q = None
#     if request.GET.get('q') is not None:
#         q = request.GET.get('q')
#         if q == 'invite':
#             employee.is_invited = True
#             employee.save()
#             return redirect('invitations')
#         else:
#             return HttpResponse('handler404')
#     context={'employee':employee}
#     return render(request, 'users/profiles.html', context)


def set_invitation(request, id):
    profile = Profile.objects.get(id=id)
    
    if request.method == 'POST':
        Invitation.objects.create(
            profile_id = profile.id,
            date = request.POST.get('date'),
            place = request.POST.get('place')
        )
        return redirect('invitations')   
    context={} 
    if profile.is_invited == False:
        return HttpResponseRedirect('handler404')
    return render(request, "company/set_inv_form.html", context)

