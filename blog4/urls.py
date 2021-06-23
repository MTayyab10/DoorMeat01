from django.urls import path
from . import views

app_name = 'blog4'

urlpatterns = [

    path('', views.index, name="index"),
    path('<str:post_title>/<int:post_id>',
         views.posts, name="posts")
]
