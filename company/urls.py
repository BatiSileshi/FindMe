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
    
    path('jobs/', views.jobs, name="jobs"),
    path('post-job/', views.post_job, name="post-job"),
    path('job/<str:pk>/', views.update_job_post, name="update-job"),
    path('job-apps/', views.job_applications, name="job-applications"),
    path('job/applicant/<str:pk>/', views.view_applicant, name="view-applicant"),

]
