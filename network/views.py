from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.core.paginator import Paginator


from .models import User


def index(request):
    return render(request, "network/index.html")

def new_post(request):
    if request.method == "POST":
        return JsonResponse({"message": "Post created successfully."}, status=201)
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)

def all_posts(request):
    pass

def edit_post(request, post_id):
    pass

def delete_post(request, post_id):
    pass

def like_post(request, post_id):
    pass

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
