# Generated by Django 2.2.5 on 2019-10-31 01:02

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191030_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='citizen',
            field=encrypted_model_fields.fields.EncryptedBooleanField(default=True),
        ),
    ]
