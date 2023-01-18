from django.db import models
from company.models import Company
from users.models import Profile

# Create your models here.

class CompanyAdmin(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    admin = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
     
     
    def __str__(self):
        return str((self.company.name, self.admin.name))

