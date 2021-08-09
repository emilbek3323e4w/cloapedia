from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register, profile

urlpatterns = [
    path('category/ <int:pk>/', category_posts, name='category_posts'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]
