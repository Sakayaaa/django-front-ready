from django.db import models
from accounts.models import UserProfile
from django.urls import reverse
from django.utils.text import slugify

class Post(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True, null=True)
    body = models.TextField()
    like = models.ManyToManyField(UserProfile, related_name='post_like', blank=True, null=True)
    dislike = models.ManyToManyField(UserProfile, related_name='post_dislike', blank=True, null=True)
    start_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})
    
    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()
    
    
    
class Comment(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    start_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_valid = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.post.title} - {self.body[:20]}"