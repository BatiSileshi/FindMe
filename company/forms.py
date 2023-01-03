from django.forms import ModelForm
from django import forms
from .models import Company
 
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['is_accepted']
        
