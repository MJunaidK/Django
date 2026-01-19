from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'caption', 'title']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'posted_by']        