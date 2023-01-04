from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('company-request', views.company_request, name="company-request"),
    path('ac-request/<str:id>/', views.accept_or_cancel_request, name="ac-request"),
    path('add-ca/', views.add_company_admin, name="add-company-admin"),
    path('delete-ca/<str:id>/', views.delete_company_admin, name="delete-company-admin"),


]
