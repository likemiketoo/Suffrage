from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import VotedUsers


# Defines the fields that appears when an admin manually adds a user
# class VoteAddForm(forms.ModelForm):
#
#     # Defines what aspects from a model this class is utilizing
#     class Meta:
#         model = VotedUsers
#         fields = ('id', 'position')
