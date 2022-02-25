# Generated by Django 4.0.2 on 2022-02-24 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0006_alter_sportsparticipant_participant_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportsparticipant',
            name='participant_event_1',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_event_1', to='sports.sportsevent'),
        ),
        migrations.AlterField(
            model_name='sportsparticipant',
            name='participant_event_2',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_event_2', to='sports.sportsevent'),
        ),
        migrations.AlterField(
            model_name='sportsparticipant',
            name='participant_event_3',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participant_event_3', to='sports.sportsevent'),
        ),
    ]