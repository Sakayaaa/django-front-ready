from django.shortcuts import render
from .models import Post, Comment


def index(request):
    return render(request, 'blog/index.html', {})


def post(request, id):
    post = Post.objects.get(id=id)
    all_comments = Comment.objects.all()
    target_comments = []
    for comment in all_comments:
        if comment.post.id == post.id:
            target_comments.append(comment)
    
    return render(request, 'blog/post.html', {'post':post, 'comments':target_comments})


def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts':posts})
