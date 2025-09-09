from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post/<int:id>', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
]
