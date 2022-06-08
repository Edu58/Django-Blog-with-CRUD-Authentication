from django.db import models

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