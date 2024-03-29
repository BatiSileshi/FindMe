from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('', views.profiles, name="profiles"),
    
    
    path('account/', views.account, name="account"),
    path('user-profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('edit-profile/', views.editProfile, name="edit-profile"),
    path('inbox/', views.inbox, name="inbox"),
    path('message/<str:pk>/', views.viewMessage, name="message"),
    path('create-message/<str:pk>/', views.createMessage, name="create-message"),
    path('add-skill', views.addSkill, name="add-skill"),
    path('update-skill/<str:pk>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<str:pk>/', views.deleteSkill, name="delete-skill"),
    
    path('news/', views.news, name="news"),
    path('news/<str:pk>/', views.single_news, name="single-news"),
    
]
