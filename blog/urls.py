from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('post/<slug:slug>/comment/', views.add_comment, name='add_comment'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('post/<slug:slug>/dislike/', views.dislike_post, name='dislike_post'),
]
