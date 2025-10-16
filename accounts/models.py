from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



class UserProfile(models.Model):
    class ProfessionalStatus(models.TextChoices):
        DEVELOPER = "Developer", "Developer"
        JUNIOR = "Junior Developer", "Junior Developer"
        SENIOR = "Senior Developer", "Senior Developer"
        MANAGER = "Manager", "Manager"
        STUDENT = "Student", "Student"
        INSTRUCTOR = "Instructor", "Instructor"
        INTERN = "Intern", "Intern"
        OTHER = "Other", "Other"
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='pfps', default='pfps/default_userprofile_picture.png')
    professional_status = models.CharField(
        max_length=40,
        choices=ProfessionalStatus.choices,
        default=ProfessionalStatus.DEVELOPER
    )
    company = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    skills = models.CharField(max_length=60)
    github_username = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField(max_length=150)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    
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


