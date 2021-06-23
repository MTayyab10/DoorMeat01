from django.db import models

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.CharField(max_length=150, blank=2 )
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title}, by {self.author}"

