from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create_post', views.new_post, name='create_post'),
    path('all_posts', views.all_posts, name='all_posts'),
    path('edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/<int:post_id>', views.delete_post, name='delete_post'),
    path('like/<int:post_id>', views.like_post, name='like_post'),
    path('unlike/<int:post_id>', views.unlike_post, name='unlike_post'),

    path('following_posts', views.following_posts, name='following_posts'),
    path('following', views.following, name='following'), #see who you are following
    path('follow/<str:username>', views.follow, name='follow'),
    path('unfollow/<str:username>', views.unfollow, name='unfollow'),
    
    path('profile/<str:username>', views.profile, name='profile'),
    path('profile/<str:username>/followers', views.followers, name='followers'), #see your or someone elses followers
    
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register")
]
