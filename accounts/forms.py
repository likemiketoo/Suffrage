from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'zip_code', 'dob')


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='A valid email address is required')

    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'zip_code', 'dob')