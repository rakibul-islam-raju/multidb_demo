from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_ROLE = (
        ('user', 'User'),
        ('editor', 'Editor'),
        ('manager', 'Manager')
    )

    role = models.CharField(max_length=10, default='user', choices=USER_ROLE)


    def __str__(self):
        return self.username
    