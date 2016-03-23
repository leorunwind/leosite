# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from leaveMsg.models import MessagePost
import re

class RegisterForm(forms.Form):
    username = forms.CharField(label='昵称', max_length=20)
    email = forms.CharField(label='邮箱', required=False)
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput())
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(u'^[\u4e00-\u9fa5 _ a-zA-Z0-9]+$',username):
            raise forms.ValidationError(username)
        try:
            User.objects.get_by_natural_key(username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('此用户名已存在')
        
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get_by_natural_key(email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('此邮箱已存在')
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('两次输入的密码不相同')
            
class MsgPostForm(forms.Form):
    title = forms.CharField(label='标题',max_length=30)
    content = forms.CharField(label='内容',widget=forms.Textarea)
    
    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            MessagePost.objects.get(title=title)
        except ObjectDoesNotExist:
            return title
        raise forms.ValidationError('此标题已存在')