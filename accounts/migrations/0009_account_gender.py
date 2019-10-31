# Generated by Django 2.2.5 on 2019-10-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_ssn'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer Not To Disclose', 'Prefer Not To Disclose')], default='Prefer Not To Disclose', max_length=23),
        ),
    ]