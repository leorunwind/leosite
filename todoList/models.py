from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.
class EventPost(models.Model):
    user = models.ForeignKey(User)
    todo = models.CharField(max_length=50)
    flag = models.IntegerField(default=1)
    priority = models.IntegerField(default=0)
    pubtime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u'%d %s %s' % (self.id, self.todo, self.flag)

    class Meta:
        ordering = ['priority', 'pubtime']
    
class EventPostAdmin(admin.ModelAdmin):
    list_display = ('user','todo','flag','priority','pubtime')
    list_filter = ('pubtime',)
    ordering = ('-pubtime',)
    
admin.site.register(EventPost,EventPostAdmin)