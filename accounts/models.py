from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    pfp = models.ImageField(upload_to='pfps')

    def __str__(self):
        return f"{self.user}"
