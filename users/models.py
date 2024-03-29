from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
   
class Profile(models.Model):
    LOOKING_FOR=(
        ('work', 'Work'),
        ('employee', 'Employee'),    
    )
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
    social_linkedin = models.CharField(max_length=200, null=True, blank=True)
    social_facebook = models.CharField(max_length=200, null=True, blank=True)
    cv = models.FileField(null=True, blank=True)
    # is_invited = models.BooleanField(default=False)
    is_cv_approved = models.BooleanField(default=False)
    is_hired = models.BooleanField(default=False)
    looking_for = models.CharField(max_length=20, null=True, choices=LOOKING_FOR)
    
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.user.username)
    
     

    
    
class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering = ['-created_at']
    
    
class Message(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return str(self.subject)
    
    class Meta:
        ordering = ['is_read', '-created_at']
    
        
    
