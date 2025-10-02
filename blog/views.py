from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import AddCommentForm, CreatePostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'blog/index.html', {})


@login_required
def posts(request):
    posts = Post.objects.all().order_by('-updated_at')
    
    for post in posts:
        post.user_liked = request.user.userprofile in post.like.all()
        post.user_disliked = request.user.userprofile in post.dislike.all()
    
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user.userprofile
            new_post.save()
            return redirect('posts')
    else:
        form = CreatePostForm()

    return render(request, 'blog/posts.html', {'posts': posts, 'form':form})

@login_required
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = AddCommentForm()
    
    # all_comments = Comment.objects.all()
    # target_comments = []
    # for comment in all_comments:
    #     if comment.post.id == post.id:
    #         target_comments.append(comment)

    return render(request, 'blog/post.html', {'post': post, 'form':form})


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.userprofile  # attach logged-in user
            comment.save()
    return redirect('post', slug=post.slug)  # always go back to the post page



@login_required
def like_post(request, slug):
    user = request.user.userprofile
    post = get_object_or_404(Post, slug=slug)
    
    if user in post.dislike.all():
        post.dislike.remove(user)
        
    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
        
    return redirect('posts')


@login_required
def dislike_post(request, slug):
    user = request.user.userprofile
    post = get_object_or_404(Post, slug=slug)
    
    if user in post.like.all():
        post.like.remove(user)
        
    if user in post.dislike.all():
        post.dislike.remove(user)
    else:
        post.dislike.add(user)
        
    return redirect('posts')