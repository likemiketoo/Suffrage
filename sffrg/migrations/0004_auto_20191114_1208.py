# Generated by Django 2.2.5 on 2019-11-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sffrg', '0003_candidate_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='avatar',
            field=models.ImageField(blank=True, default='candidate_images/placeholder.jpg', upload_to='candidate_images'),
        ),
    ]
