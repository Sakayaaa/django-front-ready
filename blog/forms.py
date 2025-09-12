from django import forms
from .models import Comment, Post

class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'cols': 30,
                'rows': 5,
                'placeholder': 'Comment on this post',
                'class': 'form-control',  # optional, for styling
            }),
        }
        
    
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        widgets = {
            'body' : forms.Textarea(attrs={
                'cols': 30,
                'rows': 5,
                'placeholder': 'Post Description',
            }),
            
            'title' : forms.TextInput(attrs={
                'placeholder': 'Post Title',
                'class': 'form-control my-1',
            }),
        }