import datetime

from django.db import models
from django.utils import timezone
from encrypted_model_fields.fields import EncryptedCharField

from accounts.models import Account

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Election Models
class Election(models.Model):
    # Title of Election
    title = models.CharField(max_length=60, unique=True)
    # Description of election
    description = models.TextField(help_text="Enter election description here", blank=True)
    # When the election posted
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


POSITION_CHOICES = (('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer'))


class Position(models.Model):
    # Gets the foreign key election from elections
    election = models.ForeignKey(Election, null=True, on_delete=models.CASCADE)
    # title = models.CharField(max_length=20)
    title = models.CharField(max_length=20, choices=POSITION_CHOICES)
    # title = models.CharField(max_length=20, choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Treasurer', 'Treasurer')], default='President')

    def __str__(self):
        return self.title


class VotedUsers(models.Model):
    id = models.CharField(max_length=100, primary_key=True, unique=True)
    position = models.IntegerField(default=0)


# Candidate Model
class Candidate(models.Model):
    # Gets the foreign key election from elections
    election = models.ForeignKey(Election, on_delete=models.CASCADE)

    position = models.ForeignKey(Position, null=True, on_delete=models.CASCADE)
    # Full nam of candidate
    full_name = models.CharField(max_length=40, unique=True)
    # Self explanatory
    description = models.TextField(default="No additional information to display.")
    website = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=2, default='VA')
    party = models.CharField(max_length=20)
    votes = models.IntegerField(default=0, editable=False)
    avatar = models.ImageField(upload_to='candidate_images', default='candidate_images/placeholder.jpg')

    def __str__(self):
        return self.full_name
        # return self
