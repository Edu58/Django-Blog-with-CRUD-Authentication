from django import forms
from .models import Post, Profile
from django.contrib.auth.models import User


class NewPostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("author","category","title","content")


class UpdatePostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","content")


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("title","content")