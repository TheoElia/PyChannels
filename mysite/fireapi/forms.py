from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import File
from django.forms import ModelForm


class FileCreationForm(ModelForm):
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    class Meta:
        model =File
        fields = ('name','file_path','img','download_url', 'date_created')
   
class FileChangeForm(ModelForm):
    class Meta:
        model = File
        fields = ('name','file_path','img','download_url', 'date_created')

