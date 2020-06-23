from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=300)
    image_url = models.URLField()
    owner = models.ForeignKey('auth.User', related_name='blogs', on_delete=models.CASCADE)