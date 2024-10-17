from django.contrib.auth.models import AbstractUser
from django.db import models

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="posts")
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField("User", blank=True, related_name="liked_posts")

    def serialize(self):
        return {
            "id": self.pk,
            "user": self.user.username,
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes.count()
        }
    
    def __str__(self):
        return f"{self.user} posted {self.content} on {self.timestamp}"
    
class Profile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE, related_name="profile")
    followers = models.ManyToManyField("User", blank=True, related_name="following")
    
    def __str__(self):
        return f"{self.user} has {self.followers.count()} followers"
    
    def serialize(self):
        return {
            "user": self.user.username,
            "followers": self.followers.count()
        }
    
    def following(self):
        return self.followers.count()
    
    def followers(self):
        return self.followers.count()

class User(AbstractUser):
    pass
