# Generated by Django 4.0.4 on 2023-08-11 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManageVideos', '0002_alter_subtitles_subtitles_alter_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='slug',
        ),
        migrations.AddField(
            model_name='video',
            name='Custom_Subtitles',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Subtitles',
        ),
    ]
