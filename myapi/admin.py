from django.contrib import admin

# Register your models here.
from .models import Blog, UserProfile

admin.site.register(Blog)
admin.site.register(UserProfile)