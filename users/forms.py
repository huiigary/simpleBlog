from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:  # Meta - gives nested namespace for configurations
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):  # Form to update the username and email
    email = forms.EmailField()

    class Meta:  # Meta - gives nested namespace for configurations
        model = User
        # these are the fields we want the form to have
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):  # From to update the image
    class Meta:
        model = Profile  # modle we want to work with
        fields = ['image']  # fields we want to work with
