# Generated by Django 4.0.4 on 2023-08-11 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ManageVideos', '0007_videodata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subtitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subtitles', models.FileField(upload_to='Subtitles')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManageVideos.video')),
            ],
        ),
        migrations.DeleteModel(
            name='VideoData',
        ),
    ]
