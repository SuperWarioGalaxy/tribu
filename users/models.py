from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    avatar = models.ImageField(upload_to='avatars/', default='noavatar.png')
    bio = models.TextField(max_length=200)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
