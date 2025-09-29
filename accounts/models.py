from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='pfps', default='pfps/default_userprofile_picture.png')
    dev_status = models.
    bio = models.TextField()

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("profile", kwargs={"id": self.id})

# ____AUTO CREATE USER PROFILE WHEN A NEW USER HAS BEEN CREATED____
# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)


class Experience(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    job = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        if self.current:
            return f"{self.job} at {self.company} (Current)"
        return f"{self.job} at {self.company}"


class Education(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    school = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        if self.current:
            return f"{self.degree} in {self.field} from {self.school} (Current)"
        return f"{self.degree} in {self.field} from {self.school}"
