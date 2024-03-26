from django.db import models
from django.contrib.auth.models import AbstractUser

def upload_image(instance, filename):
    path = f'images/{instance.username}'
    extension = path.split('.')[-1]
    if extension:
        path = path + '.' + extension
    return path

class User(AbstractUser):
    image = models.ImageField(
        upload_to=upload_image,
        null=True,
        blank=True
    )
