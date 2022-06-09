from django.db import models
from django.contrib.auth.models import User

choices = (
    ('coding', 'coding'),
    ('sports', 'sports'),
    ('technology', 'technology')
)

# Create your models here.
class Category(models.Model):
    name = models.CharField(choices=choices, max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    author = models.CharField(max_length=30, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, null=False, blank=False, related_name='posts', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def get_post_likes(self):
        return self.like_set.all().count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.post} liked by -> {self.user.username}'

    @classmethod
    def get_likes(cls, post_obj):
        return post_obj.like_set.all().count()