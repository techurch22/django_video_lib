# Generated by Django 4.1.2 on 2022-10-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_application', '0008_director_video_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Мужчина'), ('F', 'Женщина')], default='M', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='actors',
            field=models.ManyToManyField(to='video_application.actor'),
        ),
    ]
