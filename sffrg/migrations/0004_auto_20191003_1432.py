# Generated by Django 2.2.5 on 2019-10-03 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sffrg', '0003_auto_20191002_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='election',
            name='title',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
