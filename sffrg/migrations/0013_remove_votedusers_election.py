# Generated by Django 2.2.5 on 2019-10-15 01:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sffrg', '0012_auto_20191014_2144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votedusers',
            name='election',
        ),
    ]
