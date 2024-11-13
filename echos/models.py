from django.conf import settings
from django.db import models
from django.urls import reverse


# Create your models here.
class Echo(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('echos:echos-detail', kwargs={'pk': self.pk})
