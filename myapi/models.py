from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# blog model
class Blog(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    image_url = models.URLField()
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)

# profile model for User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(default=None)