from django.contrib import admin
from .models import Post


class AdminPosts(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Post, AdminPosts)