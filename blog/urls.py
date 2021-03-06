from distutils.debug import DEBUG
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<category_id>/', views.by_category, name='by_category'),
    path('profile/', views.profile, name='profile'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<id>', views.post_detail, name='post_detail'),
    path('update/<id>', views.update_post, name='post_update'),
    path('like/<post_id>', views.like_post, name='like_post'),
    path('delete/<id>', views.delete_post, name='delete_post')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
