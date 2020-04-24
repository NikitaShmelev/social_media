from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE
        )
    profile_id = models.PositiveIntegerField(
        verbose_name='User ID',
    )
    first_name = models.TextField(max_length=100, blank=True)
    second_name = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=10000, blank=True)
    birth_date = models.DateField(blank=True,null=True)
    avatar = models.ImageField(
        upload_to='profile_image',
        blank=True,
    )

    def __str__(self):
            return self.user.email
