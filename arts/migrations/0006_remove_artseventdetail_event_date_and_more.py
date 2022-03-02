# Generated by Django 4.0.2 on 2022-02-25 17:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0005_alter_artseventdetail_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artseventdetail',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='artseventdetail',
            name='event_time',
        ),
        migrations.AddField(
            model_name='artseventdetail',
            name='event_dateTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]