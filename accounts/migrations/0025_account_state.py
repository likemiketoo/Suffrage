# Generated by Django 2.2.5 on 2019-11-05 22:56

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_auto_20191105_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='state',
            field=encrypted_model_fields.fields.EncryptedCharField(default='VA'),
            preserve_default=False,
        ),
    ]
