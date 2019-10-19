# Generated by Django 2.2.5 on 2019-10-19 20:10

from django.db import migrations
import encrypted_model_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20191019_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='dob',
            field=encrypted_model_fields.fields.EncryptedDateField(verbose_name='date of birth'),
        ),
    ]