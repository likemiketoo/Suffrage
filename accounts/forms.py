from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


class AccountCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'zip_code', 'dob')


# Uses prebuilt registration form from Django UserCreationForm
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='A valid email address is required')

    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'zip_code', 'dob')


# Uses custom form
class AccountAuthenticationForm(forms.ModelForm):
    # Stops password from being visible when typing
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # Specifies whats aspects of a class i'm borrowing
    class Meta:
        model = Account
        fields = ('email', 'password')

    # Gets form info before it's passed to provide feedback
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Login is not valid, please try again.')
