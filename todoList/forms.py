# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from todoList.models import EventPost
import re
            
class EventPostForm(forms.Form):
    title = forms.CharField(label='标题',max_length=30)
    detail = forms.CharField(label='内容',widget=forms.Textarea)
    
    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            EventPost.objects.get(title=title)
        except ObjectDoesNotExist:
            return title
        raise forms.ValidationError('此标题已存在')