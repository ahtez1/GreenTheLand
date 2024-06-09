from django.contrib import admin
from .models import FAQ, Feedback, Gallery, NewsUpdates, Post, Project, Comment, Stats

# Register your models here.
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['image']
    

@admin.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display= ['trees_planted', 'high_schools', 'primary_schools']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    search_fields = ['title', 'description']
    list_filter = ['created_at', 'updated_at']



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    search_fields = ['name', 'description']
    list_filter = ['start_date', 'end_date']



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'created_at']
    search_fields = ['post__title', 'author__username']
    list_filter = ['created_at']
    


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    search_fields = ['question']


@admin.register(NewsUpdates)
class NUpdatesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'created_at', 'pics'] 


@admin.register(Feedback)
class FBackAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'pics']