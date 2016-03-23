from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

# Create your models here.
#修改这里的MessagePost后migrate数据库,see http://www.tuicool.com/articles/UbmQbm
class MessagePost(models.Model):

    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50,blank = True)    
    content = models.TextField(blank = True,null = True)
    pubtime = models.DateTimeField()
    
    def get_absolute_url(self):
        path = reverse('detail',kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s"%path
    
    def __str__(self) :
        return self.title
        
    class Meta:
        ordering = ('-pubtime',)
    
class MessagePostAdmin(admin.ModelAdmin):
    list_display = ('pubtime','title')
    
admin.site.register(MessagePost,MessagePostAdmin)
# Create your models here.
