from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

class MusicianForm(ModelForm):
    class Meta:
        model = Musician
        fields = '__all__'
        exclude = ['user', 'like']
