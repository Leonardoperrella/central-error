from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from stone.core.models import CustomUser, Error


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1']


class ErrorForm(forms.ModelForm):
    class Meta:
        model = Error
        fields = ['enviroment', 'level', 'log', 'events']
