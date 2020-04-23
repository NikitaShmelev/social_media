from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class SignupForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required', 
                            widget=forms.PasswordInput(attrs={
                                'placeholder':'Email', 
                                'type':'email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
        )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation'})
        )
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Username'})
        )
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        

class ProfileForm(forms.ModelForm):

    bio = forms.Textarea()
    avatar = forms.ImageField()

    class Meta:
        model = UserProfile
        fields = ('bio', 'avatar')