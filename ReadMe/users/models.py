from django.db import models
from django.contrib.auth.models import AbstractUser


def user_media_path(instance, filename):
    new_filename = f"photo.{filename.split('.')[-1]}"
    return f'user/{instance.username}/{new_filename}' 


class User(AbstractUser):
    image = models.ImageField(upload_to=user_media_path, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")