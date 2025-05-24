from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import *


class Register_form(UserCreationForm):
    class Meta():
        model = Polbzovatelb
        fields = ['username', 'password1', 'password2', 'email', 'address', 'phone']


class Wish_form(forms.ModelForm):
    class Meta():
        model = Wish
        fields = ["name", "description", "image"]


class Profile_form(UserChangeForm):
    class Meta():
        model = Polbzovatelb
        fields = ['username', 'address', 'phone']