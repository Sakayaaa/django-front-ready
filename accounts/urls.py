from django.urls import path
from . import views

urlpatterns = [
    path('education/add/', views.add_education, name='add_education'),
    path('education/<int:id>/edit/', views.edit_education, name='edit_education'),
    path('education/<int:id>/delete/', views.delete_education, name='delete_education'),
    
    path("experience/add/", views.add_experience, name="add_experience"),
    path("experience/<int:id>/edit/", views.edit_experience, name="edit_experience"),
    path("experience/<int:id>/delete/", views.delete_experience, name="delete_experience"),
    
    path('create-profile/', views.create_profile, name='create_profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('register/', views.register, name='register'),
    path('delete-account/', views.delete_account, name='delete_account'),
]
