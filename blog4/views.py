from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, "blog4/index.html", {
        "posts": posts
    })


def posts(request, post_id, post_title):
    posts = Post.objects.get(title=post_title, pk=post_id)
    # post_title = Post.objects.get(title=post_title)

    return render(request, "blog4/singleBlog.html", {
        "posts": posts
    })
