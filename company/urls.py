from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_company, name="register-company"),
    path('welcome/', views.welcome_company, name="welcome-company"),
    path('about-company/', views.about_company, name="about-company"),

]
