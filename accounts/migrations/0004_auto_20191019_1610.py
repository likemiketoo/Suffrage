# Generated by Django 2.2.5 on 2019-10-19 20:10

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20191019_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='zip_code',
            field=encrypted_model_fields.fields.EncryptedCharField(blank=True, null=True),
        ),
    ]
