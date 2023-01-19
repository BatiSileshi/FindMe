from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_company, name="register-company"),
    path('welcome/', views.welcome_company, name="welcome-company"),
    path('company-home/', views.company_home, name="company-home"),
    path('invitations/', views.invitations, name="invitations"),
    # path('invite/', views.invite, name="invite"),
    #path('invite-final/<str:id>/', views.invite_final, name="invite-final"),
    path('set-invitation/<str:id>/', views.set_invitation, name="set-invitation"),

]
