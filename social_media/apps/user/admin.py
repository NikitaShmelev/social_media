from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile
from .forms import ProfileForm


@admin.register(UserProfile)
class ProfilekAdmin(admin.ModelAdmin):
    list_display = (
        'profile_id', 'user',
        'first_name', 'second_name',
        'birth_date', 'bio',
        'avatar',
        )
    form = ProfileForm