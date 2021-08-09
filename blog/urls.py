from .base.html import search
from django.urls import path
from .views import main_page, create_post

urlpatterns = [
    path('category/<int:pk>/', category_posts, name = 'category_details'),
    path('my-posts/', my_posts, name='my_posts'),
    path('create-post', create_post, name='post_create'),
    path('', main_page, name='main_page'),
]
