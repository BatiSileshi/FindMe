
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

def createProfile(sender, instance, created, **kwargs):
    if created:
        user=instance
        profile = Profile.objects.create(
            user=user,
            # username=user.username,
            email=user.email,
            name=user.first_name,
        )
        
        subject = ' Welcome to FindME platform!'
        message = ' We are glad that you are here!'
         
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently =False,
        )
        
        
def editProfile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.name = profile.user
        user.email = profile.email
        user.save()
        
        
        subject = ' Welcome to FindME platform!'
        message = ' You have successfully updated your profile'
         
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently =False,
        )
        
        
def deleteUser(sender, instance, **kwargs):
    try:
        user=instance.user
        user.delete()
    except:
        pass
    
        
post_save.connect(createProfile, sender=User)
post_save.connect(editProfile, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)