# Generated by Django 2.2.5 on 2019-11-05 15:25

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20191102_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='citizen',
            field=encrypted_model_fields.fields.EncryptedCharField(default=True),
        ),
    ]
