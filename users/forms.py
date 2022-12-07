from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Message, Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model= User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class MessageForm(ModelForm):
    class Meta:
        model= Message
        fields =['name', 'email', 'subject', 'body']
         
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})