from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import ProfileForm


@admin.register(UserProfile)
class ProfilekAdmin(admin.ModelAdmin):
    list_display = (
        'profile_id',
        'user',
        'bio',
        'avatar',
        )
    form = ProfileForm