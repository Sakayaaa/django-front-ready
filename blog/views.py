from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import AddCommentForm, CreatePostForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'blog/index.html', {})


@login_required
def posts(request):
    posts = Post.objects.all().order_by('-updated_at')
    
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


def post(request, id):
    post = Post.objects.get(id=id)
    form = AddCommentForm()
    
    # all_comments = Comment.objects.all()
    # target_comments = []
    # for comment in all_comments:
    #     if comment.post.id == post.id:
    #         target_comments.append(comment)

    return render(request, 'blog/post.html', {'post': post, 'form':form})


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    if request.method == "POST":
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user.userprofile  # attach logged-in user
            comment.save()
    return redirect('post', id=post.id)  # always go back to the post page