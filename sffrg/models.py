import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Election Models
class Election(models.Model):
    # Title of Election
    title = models.CharField(max_length=60)
    # Description of election
    description = models.TextField(help_text="Enter election description here", blank=True)
    # When the election posted
    pub_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


# Candidate Model
class Candidate(models.Model):
    # Gets the foreign key election from elections
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    # Full nam of candidate
    full_name = models.CharField(max_length=40)
    # Self explanatory
    state = models.CharField(max_length=2, default='VA')
    party = models.CharField(max_length=20)
    votes = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.full_name


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#     def __str__(self):
#         return self.question_text
#
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
#     was_published_recently.admin_order_field = 'pub_date'
#     was_published_recently.boolean = True
#     was_published_recently.short_description = 'Published recently?'
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#
#     def __str__(self):
#         return self.choice_text

