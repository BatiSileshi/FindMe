from django.forms import ModelForm
from django import forms
from .models import Company, Invitation
 
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['is_accepted']
        
class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ['profile']