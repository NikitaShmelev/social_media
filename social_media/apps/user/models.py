from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_id = models.PositiveIntegerField(
        verbose_name='User ID',
    )
    bio = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(
        upload_to='profile_image',
        blank=True,
    )

    def __str__(self):
            return self.user.email
