from django.forms import ModelForm, widgets
from django import forms
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields='__all__'
        
        # creating checkbox for many to many fields
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }