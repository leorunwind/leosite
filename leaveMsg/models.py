from django.db import models
from django.contrib import admin
# Create your models here.
#修改这里的MessagePost后migrate数据库,see http://www.tuicool.com/articles/UbmQbm
class MessagePost(models.Model):
    user = models.CharField(max_length = 50)
    email = models.EmailField()
    title = models.CharField(max_length = 30,blank=True)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-datetime',)
    
class MessagePostAdmin(admin.ModelAdmin):
    display_li = ('datetime','user','title')
    
admin.site.register(MessagePost,MessagePostAdmin)