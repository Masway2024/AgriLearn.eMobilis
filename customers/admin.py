from django.contrib import admin
from .models import Customer,  ServiceItem, TeamMember, Post, Video


# Register models for the admin interface
admin.site.register(Customer)
admin.site.register(ServiceItem)


# TeamMember Admin
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'image']
    search_fields = ['name', 'position']
    list_filter = ['position']

# Post Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_published', 'category')
    search_fields = ('title', 'author', 'category')
    list_filter = ('category', 'author', 'date_published')

# Video Admin
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'youtube_url', 'created_at')
    search_fields = ('title',)


