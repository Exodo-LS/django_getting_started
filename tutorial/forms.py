from django import forms
from django.forms import ModelForm

from .models import *


class LessonForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add new task...'}))

    class Meta:
        model = Lesson
        fields = '__all__'
