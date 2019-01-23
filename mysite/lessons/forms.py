from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Lesson,Comment
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from froala_editor.widgets import FroalaEditor
from ckeditor.widgets import CKEditorWidget


class LessonCreationForm(ModelForm):
    body=forms.CharField(widget=CKEditorWidget())#(widget=FroalaEditor)
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    class Meta:
        model =Lesson
        fields = ('title','intro_text','body','lesson_img')

class CommentCreationForm(ModelForm):
    #body=forms.CharField(widget=FroalaEditor)
    # username = forms.CharField(max_length=200,
    # widget=(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})))
    class Meta:
        model = Comment
        fields = ('comment','module',)


class LessonChangeForm(ModelForm):
    body=forms.CharField(widget=CKEditorWidget())#(widget=FroalaEditor)
    class Meta:
        model = Lesson
        fields = ('title','intro_text','lesson_img','body','reviewed','date_created')
