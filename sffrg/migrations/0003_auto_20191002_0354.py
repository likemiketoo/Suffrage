# Generated by Django 2.2.5 on 2019-10-02 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sffrg', '0002_election_total_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sffrg.Election'),
        ),
    ]