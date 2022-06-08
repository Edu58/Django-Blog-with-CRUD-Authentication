from multiprocessing import context
from webbrowser import get
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from.forms import NewPostForm, UpdatePostForm


# Create your views here.
def home(request):
    all_posts = Post.objects.all()

    context = {'posts':all_posts}
    return render(request, 'index.html', context)


def by_category(request, category_id):
    all_in_category = Post.objects.filter(category__id=category_id)

    context = {'posts':all_in_category}

    return render(request, 'category.html', context)


def add_post(request):
    form = NewPostForm()

    if request.method == "POST":
        form = NewPostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    
    return render(request, 'add_post.html', context)


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)

    context = {'post': post}

    return render(request, 'post_detail.html', context)


def update_post(request, id):
    post = get_object_or_404(Post, pk=id)

    form = UpdatePostForm(instance=post)

    if request.method == "POST":
        form = UpdatePostForm(request.POST, instance=post)

        if form.is_valid():
            post.save()
            return redirect('home')
    
    context = {'form': form}
    
    return render(request, 'update_post.html', context)


def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)

    if post:
        post.delete()
        return redirect('home')
