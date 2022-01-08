from django import forms
from django import forms
from django.forms import fields
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ListForm(forms.ModelForm):
    class Meta:
        model = list
        fields = ["item", "complete", "due_date", "status"]


class AddUser(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["photo", "username", "password1","password2", "email"]
    