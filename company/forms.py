from django.forms import ModelForm
from django import forms
from .models import Company, Invitation, JobPost, JobApplication
 
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        exclude = ['is_accepted']
        
class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ['profile']
        
class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        exclude = ['company']
        
        
        
class JobApplicationForm(ModelForm):
    class Meta:
        model=JobApplication
        exclude = ['profile', 'company']