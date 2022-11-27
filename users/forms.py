from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        

class MessageForm(ModelForm):
    class Meta:
        model= Message
        fields =['name', 'email', 'subject', 'body']
         