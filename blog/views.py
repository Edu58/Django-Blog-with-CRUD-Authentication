from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Category, Post, Like
from.forms import NewPostForm, UpdatePostForm, UserUpdateForm, ProfileUpdateForm


@login_required(login_url='accounts/login/')
def home(request):
    all_posts = Post.objects.all()

    context = {'posts':all_posts}
    return render(request, 'index.html', context)


@login_required(login_url='accounts/login/')
def by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    all_in_category = Post.objects.filter(category__id=category_id)

    context = {'posts':all_in_category, 'category': category}

    return render(request, 'category.html', context)


@login_required(login_url='accounts/login/')
def add_post(request):
    form = NewPostForm()

    if request.method == "POST":
        form = NewPostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    context = {'form': form}
    
    return render(request, 'add_post.html', context)


@login_required(login_url='accounts/login/')
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    likes = post.get_post_likes()

    # liked = False
    # if post:
    #     if post.likes.filter(id=request.user.id).exists():
    #         post.likes.remove(request.user)
    #         liked = False
    #     else:
    #         post.likes.add(request.user)
    #         liked = True

    context = {'post': post, 'likes': likes}

    return render(request, 'post_detail.html', context)


@login_required(login_url='accounts/login/')
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


@login_required(login_url='accounts/login/')
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)

    if post:
        post.delete()
        return redirect('home')


@login_required(login_url='accounts/login/')
def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    new_like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        new_like.delete()

    return redirect(reverse('home'))


# def like_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)

#     liked = False
#     if post:
#         if post.likes.filter(id=request.user.id).exists():
#             post.likes.remove(request.user)
#             liked = False
#         else:
#             post.likes.add(request.user)
#             liked = True

#     return redirect(reverse('post_detail', args=[str(post_id)]))


@login_required(login_url='accounts/login/')
def profile(request):

    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'prof_form': profile_form
    }

    return render(request, 'profile.html', context)