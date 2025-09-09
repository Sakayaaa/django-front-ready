from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('posts/', views.posts, name='posts'),
    path('post/<int:id>', views.post, name='post'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
]
