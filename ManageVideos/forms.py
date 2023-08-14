from django import forms
from .models import Video
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# create a ModelForm

class UploadVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','password1', 'password2']
        




