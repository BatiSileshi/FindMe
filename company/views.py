from django.shortcuts import render, redirect
from .forms import CompanyForm
from django.contrib import messages

# Create your views here.
def register_company(request):

    form = CompanyForm(request.POST) 
    if request.method=='POST':
        form=CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully register your company.")
            return redirect('work-with-us')

        else:
            messages.error(request, "Error occurred")
    context={'form':form}
    return render(request, 'company/form.html', context)