# Generated by Django 2.2.5 on 2019-11-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sffrg', '0007_candidate_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='website',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
