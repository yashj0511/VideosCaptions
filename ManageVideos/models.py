from django.db import models

# Create your models here.

class Video(models.Model):
    title=models.CharField(max_length=100,blank=True,null=True)
    Video=models.FileField(upload_to='Video')
    slug=models.SlugField(unique=True,blank=True,null=True)
    subtitles_file = models.FileField(upload_to='Subtitles', null=True, blank=True)
    timestamp_start=models.CharField(max_length=100,blank=True,null=True)
    timestamp_end=models.CharField(max_length=100,blank=True,null=True)
    subtitles_text=models.CharField(max_length=100,null=True,blank=True)
       
    def __str__(self):
         return self.slug



   
