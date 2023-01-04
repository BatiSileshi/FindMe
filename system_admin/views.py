from django.shortcuts import render, redirect
from django.contrib import messages
from company.models import Company
from django.http import HttpResponse
from.models import CompanyAdmin
from .forms import CompanyAdminForm
# Create your views here.

def home(request):
    context={}
    return render(request, 'system_admin/home.html', context)


def company_request(request):
    companies = Company.objects.all()
    company_admins = CompanyAdmin.objects.all()
    context={'companies':companies, 'company_admins':company_admins}
    return render(request, 'system_admin/company_request.html', context)



def accept_or_cancel_request(request, id):
    company = Company.objects.get(id=id)
    
    q = None
    if request.GET.get('q') is not None:
        q = request.GET.get('q')
        if q == 'accept':
            company.is_accepted = True
            company.save()
            return redirect('company-request')
        elif q == 'cancel':
            company.is_accepted = False
            company.save()
            return redirect('company-request')
        else:
            return HttpResponse('handler404')
    context={'company':company}
    return render(request, 'system_admin/company_request.html', context)


######################
# MANAGING COMPANY ADMIN
#


def add_company_admin(request):
    
    form = CompanyAdminForm()
    if request.method == "POST":
        form = CompanyAdminForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added company admin')
            return redirect('company-request')
        else:
            messages.warning(request, 'There was an error during adding company admin')
    context={'form':form}
    return render(request, 'system_admin/form.html', context)


def delete_company_admin(request, id):

    company_admin = CompanyAdmin.objects.get(id=id)
     
    if request.method == "POST":
        if company_admin.delete():
            messages.success(request, 'You have successfully deleted the selected company admin ')
            return redirect('company-request')
        else:
            messages.warning(request,'There was an error during deleting the selected hotel admin')
    context = {'object': company_admin}
    return render(request, 'system_admin/delete.html', context)