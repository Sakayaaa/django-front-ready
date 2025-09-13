from django.contrib import admin
from .models import UserProfile, Experience, Education

admin.site.register([UserProfile, Experience, Education])