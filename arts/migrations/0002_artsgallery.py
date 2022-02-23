# Generated by Django 4.0.2 on 2022-02-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtsGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=100)),
                ('image_desc', models.TextField()),
                ('image_file', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
