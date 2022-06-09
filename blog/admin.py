from django.contrib import admin
from .models import Category, Post, Like, Profile

# Register your models here.
admin.site.register([
    Category,
    Post,
    Like,
    Profile
    ])