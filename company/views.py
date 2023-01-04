from django.shortcuts import render, redirect
from .forms import CompanyForm
from .models import Company
from django.http import HttpResponse
from system_admin.models import CompanyAdmin
from django.contrib import messages

# Create your views here.
def register_company(request):
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
    return render(request, 'company/form.html', context)



def welcome_company(request):

    context={}
    
    return render(request, 'company/welcome_company.html', context)


def about_company(request):
    profile = request.user.profile
    company_admin = CompanyAdmin.objects.get(admin=profile)
    company = company_admin.company
    
    context={'company':company}
    if profile != company_admin.admin:
        return HttpResponse('handler404')
    return render(request, 'company/about_company.html', context)