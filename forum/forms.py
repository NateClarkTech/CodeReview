from .models import *;
from django import forms
from django.contrib.auth.models import User

#form to create a new thread
class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'content']
        
#form to create a new comment        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']