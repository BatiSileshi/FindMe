from django.contrib import admin
from .models import Company, Invitation, JobPost
# Register your models here.

admin.site.register(Company)
admin.site.register(Invitation)
admin.site.register(JobPost)