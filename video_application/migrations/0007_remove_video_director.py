# Generated by Django 4.1.2 on 2022-10-24 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video_application', '0006_video_director_alter_video_budget'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='director',
        ),
    ]
