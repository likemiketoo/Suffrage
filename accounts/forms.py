from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'zip_code', 'dob')
