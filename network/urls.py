from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import handler404
from .views import custom_404

from . import views

handler404 = custom_404

urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path('create_post', login_required(views.new_post), name='create_post'),
    path('all_posts', views.all_posts, name='all_posts'),
    path('edit/<int:post_id>', login_required(views.edit_post), name='edit_post'),
    #path('delete/<int:post_id>', views.delete_post, name='delete_post'),
    path('like/<int:post_id>', login_required(views.like_post), name='like_post'),

    path('following', login_required(views.following_posts), name='following'), #see who you are following
    path('follow/<str:username>', login_required(views.follow), name='follow'),
    path('unfollow/<str:username>', login_required(views.unfollow), name='unfollow'),
    
    path('profile/<str:username>', views.profile, name='profile'),
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
