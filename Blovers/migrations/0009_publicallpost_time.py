# Generated by Django 2.0.2 on 2018-03-28 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blovers', '0008_registrationlist_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicallpost',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
