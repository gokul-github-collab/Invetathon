from django import forms
from .models import Comment, Module

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ModuleForm(forms.ModelForm):
    class Meta:
        model = Module
        fields = ['title',"description", 'image']