# Generated by Django 4.1.2 on 2022-10-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_application', '0002_video_budget_video_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
