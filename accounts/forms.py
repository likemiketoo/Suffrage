from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Account


# Defines the fields that appears when an admin manually adds a user
class AccountCreationForm(UserCreationForm):

    # Defines what aspects from a model this class is utilizing
    class Meta:
        model = Account
        fields = ('email', 'first_name', 'last_name', 'username', 'zip_code', 'dob')


# Defines how the registration screen is presented to the user
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='A valid email address is required')
    # ssn = forms.CharField(max_length=9, widget=forms.HiddenInput())

    # def clean(self):
    #     cd = self.cleaned_data
    #     if cd.get('password') != cd.get('password_confirm'):
    #         self.add_error('password_confirm', "passwords do not match !")
    #     return cd

    def clean(self):
        dat = self.cleaned_data
        zipco = str(dat.get('zip_code'))
        if not zipco.isdigit():
            self.add_error('zip_code', "You must enter a valid zip code")

        if dat.get('disqualified') is True and dat.get('restored') is False:
            self.add_error('restored', "You are not eligible to vote")

        if dat.get('sig') is False:
            self.add_error('sig', "Your electronic signature is required")

        return dat

    # Defines what aspects from a model this class is utilizing
    class Meta:
        model = Account
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'zip_code', 'dob')


# Defines how the accounts are presented and authenticated when logging in
class AccountAuthenticationForm(forms.ModelForm):
    # Stops password from being visible when typing
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    # Specifies whats aspects of a class this class is borrowing
    class Meta:
        model = Account
        fields = ('email', 'password')

    # Defines what aspects from a model this class is utilizing
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError('Login is not valid, please try again.')


# Defines how an account is presented in the admin page and what aspects are changeable
class AccountUpdateForm(forms.ModelForm):

    # Defines what aspects from a model this class is utilizing
    class Meta:
        model = Account
        fields = ('email', 'username', 'zip_code')
        readonly_fields = ('zip_code')


    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            # Checks to see if account exists, excluding the instance we're in right now
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
            except Account.DoesNotExist:
                return email
            raise forms.ValidationError('Email "%s" is already in use.' % account.email)

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            # Checks to see if account exists, excluding the instance we're in right now
            try:
                account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
            except Account.DoesNotExist:
                return username
            raise forms.ValidationError('Username "%s" is already in use.' % account.username)
