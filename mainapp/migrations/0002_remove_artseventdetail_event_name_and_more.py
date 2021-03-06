# Generated by Django 4.0.2 on 2022-02-23 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artseventdetail',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='artsparticipant',
            name='participant_event_1',
        ),
        migrations.RemoveField(
            model_name='artsparticipant',
            name='participant_event_2',
        ),
        migrations.RemoveField(
            model_name='artsparticipant',
            name='participant_event_3',
        ),
        migrations.RemoveField(
            model_name='artsparticipant',
            name='participant_house',
        ),
        migrations.RemoveField(
            model_name='sportseventdetail',
            name='event_name',
        ),
        migrations.RemoveField(
            model_name='sportsparticipant',
            name='participant_event_1',
        ),
        migrations.RemoveField(
            model_name='sportsparticipant',
            name='participant_event_2',
        ),
        migrations.RemoveField(
            model_name='sportsparticipant',
            name='participant_event_3',
        ),
        migrations.RemoveField(
            model_name='sportsparticipant',
            name='participant_house',
        ),
        migrations.DeleteModel(
            name='ArtsEvent',
        ),
        migrations.DeleteModel(
            name='ArtsEventDetail',
        ),
        migrations.DeleteModel(
            name='ArtsParticipant',
        ),
        migrations.DeleteModel(
            name='House',
        ),
        migrations.DeleteModel(
            name='SportsEvent',
        ),
        migrations.DeleteModel(
            name='SportsEventDetail',
        ),
        migrations.DeleteModel(
            name='SportsParticipant',
        ),
    ]
