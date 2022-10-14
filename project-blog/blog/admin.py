from django.contrib import admin
from .models import Category, State, City, Post
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state', 'created_at', 'updated_at']
    search_fields = ['name', 'state__name']
    list_filter = ['state']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'city', 'category', 'created_at', 'updated_at', 'published']
    search_fields = ['title', 'subtitle', 'content', 'city__name', 'category__name']
    list_filter = ['city', 'category', 'published']


