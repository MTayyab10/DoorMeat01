from django.db import models


class Contact(models.Model):
    username = models.CharField(max_length=60)
    mobile = models.IntegerField()
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.username} {self.email}"
