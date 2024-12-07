from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

# models.py
from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']  # Orders the posts by the latest first

# models.py
from django.db import models

class ServiceItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    image = models.ImageField(upload_to='services/')  # Path to upload images
    link = models.URLField(blank=True, null=True)  # Optional link for each service

    def __str__(self):
        return self.title

from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=255)
    youtube_url = models.URLField(help_text="Full YouTube embed URL (e.g., https://www.youtube.com/embed/video_id)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




