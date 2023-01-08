from django.db import models
from users.models import Profile
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Invitation(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(null=True, blank=True)
    place = models.CharField(max_length=200, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    
    def __str__(self):
        return self.profile.name
    
    
    