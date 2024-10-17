from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from .models import User, Post


def index(request):
    return render(request, "network/index.html")

def new_post(request):
    if request.method == "POST":
        print("POST request received")
        content = request.POST.get("content")
        if content:
            post = Post(user=request.user, content=content)
            post.save()
            return JsonResponse({"message": "Post created successfully."}, status=201)
        else:
            return JsonResponse({"error": "Content is required."}, status=400)
    else:
        print("GET request received")
        return render(request, "network/new_post.html")

def all_posts(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, "network/all_posts.html", {"posts": posts})
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)

def edit_post(request, post_id):
    if request.method == "POST":
        try: 
            data = json.loads(request.body)
            content = data.get("content")
            print("Content: ", content)
            post = Post.objects.get(id=post_id)
            post.content = content
            if content:
                post.save()
                print("Post edited successfully.")
                return JsonResponse({"message": "Post edited successfully.", "new_content": post.content, "success": True}, status=201)
            else:
                return JsonResponse({"error": "Content is required."}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)
        
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)

def delete_post(request, post_id):
    pass

def like_post(request, post_id):
    print("like_post called")
    post = Post.objects.get(id=post_id)
    # Toggle like
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Remove user from likes
        message = "Post unliked successfully."
    else:
        post.likes.add(request.user)  # Add user to likes
        message = "Post liked successfully."
    print("Post Like Count: ", post.likes.count())
    return JsonResponse({"message": message, "new_like_count": post.likes.count(), "success": True}, status=201)

def unlike_post(request, post_id):
    pass

def following_posts(request):
    pass

def following(request):
    pass

def follow(request, username):
    pass

def unfollow(request, username):
    pass

def profile(request, username):
    pass

def followers(request, username):
    pass

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
