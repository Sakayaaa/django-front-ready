from django import forms
from .models import Comment

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