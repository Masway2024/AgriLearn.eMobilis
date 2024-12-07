
from django.contrib import messages
from django.http import HttpResponse
from customers.forms import CustomerForm, SubscriptionForm


# Gallery page
def gallery(request):
    # Fetch all service items from the database
    service_items = ServiceItem.objects.all()

    # Pass the service items to the template
    return render(request, 'gallery.html', {'service_items': service_items})



def blog(request):
    return render(request, 'blog.html')


# Contact Page
def contact(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent Successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Error submitting form. Please try again.')
    else:
        form = CustomerForm()

    return render(request, 'contact.html', {'form': form})


# About page
def about(request):
    team_members = TeamMember.objects.all()  # Fetch all team members
    return render(request, 'about.html', {'team_members': team_members})

def blog(request):
    # Fetching all posts from the database
    posts = Post.objects.all()

    # Passing posts to the template
    return render(request, 'blog.html', {'posts': posts})


# Services page
def services(request):
    return render(request, 'services.html')


# Testimonials page
def testimonials(request):
    return render(request, 'testimonials.html')


# Terms page
def terms(request):
    return render(request, 'terms.html')

# Privacy page
def privacy(request):
    return render(request, 'privacy.html')


# Video view based on video ID
def video(request):
    videos = Video.objects.all().order_by('-created_at') # Fetch videos in reverse chronological order

    return render(request, 'video.html', {'videos': videos})

def index(request):
    return render(request, 'index.html')


# views.py
from django.shortcuts import render, redirect
from .models import TeamMember

def team_view(request):
    pass

from django.shortcuts import render
from .models import Post

def recent_posts(request):
    pass


# views.py
from django.shortcuts import render
from .models import ServiceItem

def service_items_view(request):
    pass

from django.shortcuts import render
from .models import Video

def video_gallery(request):
    pass