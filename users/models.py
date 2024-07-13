from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.ImageField(upload_to='user_images/', default='profil_pic.jpg')

    def __str__(self) -> str:
        return f'{self.username}'