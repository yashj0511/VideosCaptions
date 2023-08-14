# Generated by Django 4.0.4 on 2023-08-11 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video', models.FileField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subtitles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subtitles', models.FileField(upload_to='')),
                ('slug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ManageVideos.video')),
            ],
        ),
    ]