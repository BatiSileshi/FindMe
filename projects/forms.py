from django.forms import ModelForm, widgets
from django import forms
from .models import Project, Review
 
class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['owner','review_total','review_ratio']
        
        # creating checkbox for many to many fields
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class ReviewForm(ModelForm):
    class Meta:
        model=Review
        fields= ['value', 'body']
        
        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment'
        }