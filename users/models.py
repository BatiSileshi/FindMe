from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=300, null=True, blank=True)
    short_intro= models.CharField(max_length=300, null=True, blank=True)
    bio= models.TextField(null=True, blank=True)
    profile_image= models.ImageField(null=True, blank=True, upload_to='profiles/', default='profiles/comedy.png')
    social_github = models.CharField(max_length=200, null=True, blank=True)
    telegram = models.CharField(max_length=200, null=True, blank=True)
    social_youtube = models.CharField(max_length=200, null=True, blank=True)
    social_website = models.CharField(max_length=200, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.user.username)
        
    
