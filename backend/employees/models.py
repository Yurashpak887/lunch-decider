from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    # версія мобільного застосунку
    build_version = models.CharField(max_length=10, default="1.0")

    def __str__(self):
        return self.username
