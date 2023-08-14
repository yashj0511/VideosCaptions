import os
from django.conf import settings
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from .forms import UploadVideoForm,UserRegisterForm
from . import models
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
# Create your views here.
def home(request):
    video=models.Video.objects.all()
    return render(request,'home.html',{'video':video})


# def home(request):
# def home(request):
#     videos = models.Video.objects.all()
#     video_data = [
#         {'title': video.title, 'video_url': video.Video.url,'subtitles_url': video.subtitles_file.url if video.subtitles_file else '',}
#         for video in videos
#     ]
#     video_json = json.dumps(video_data)
#     return render(request, 'home.html', {'video_json': video_json})

@login_required
def UploadVideo(request):
    if request.method=='POST':
        form=UploadVideoForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            print('form is vslid')
            return redirect('/')
    else:
        form=UploadVideoForm()
    return render(request,'UploadVideo.html',{'form':form})



# def EditSubs(request,slug):
#     obj=models.Video.objects.filter(slug=slug)
#     if request.method=='POST':
#         form=UploadVideoForm(request.POST or None ,request.FILES or None,instance=obj[0])
#         if(form.is_valid()):
#             form.save()
#             print('form is vslid')
#             return redirect('/')
#     else:
#         form=UploadVideoForm(request.POST or None ,request.FILES or None,instance=obj[0])

    

#     return render(request,'EditSubs.html',{'form':form})


def format_subtitle_entry(start, end, text):
    return f"{start} --> {end}\n{text}\n"



def EditSubs(request, slug):
    obj = models.Video.objects.filter(slug=slug).first()

    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            timestamp_start = form.cleaned_data.get('timestamp_start', '')
            print(timestamp_start)
            timestamp_end = form.cleaned_data.get('timestamp_end', '')
            print(timestamp_end)
            subtitles_text = form.cleaned_data.get('subtitles_text', '')
            print(subtitles_text)

            formatted_subtitle = format_subtitle_entry(timestamp_start, timestamp_end, subtitles_text)

            subtitles_file = obj.subtitles_file
            if subtitles_file:
                with open(subtitles_file.path, 'a') as file:
                    file.write(f'{formatted_subtitle}')
            else:
                new_subtitles_file = os.path.join(settings.MEDIA_ROOT, 'Subtitles', f'{obj.slug}.vtt')
                with open(new_subtitles_file, 'w') as file:
                    file.write(f'WEBVTT\n\n{formatted_subtitle}')

                obj.subtitles_file = new_subtitles_file
                obj.save()
            form.save()
            return redirect('home')
    else:
        form = UploadVideoForm(instance=obj)

    return render(request, 'EditSubs.html', {'form': form})



def Docs(request):
    return render(request,"docs.html")