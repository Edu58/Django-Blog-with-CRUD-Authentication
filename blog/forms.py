from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("author","category","title","content")


class UpdatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","content")
