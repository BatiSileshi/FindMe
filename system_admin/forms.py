from django.forms import ModelForm
from .models import CompanyAdmin
 
class CompanyAdminForm(ModelForm):
    class Meta:
        model = CompanyAdmin
        fields = '__all__'
        
