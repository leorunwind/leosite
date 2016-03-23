"""comment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse as res
#从三个app文件夹里的view.py文件导入函数，实现指定url到后台的交互
from leaveMsg.view import archive,main,register_page,msg_post_page
from todoList.views import event_list_page,event_post_page
from blog.views import blog_list,detail,search_tag,archives,blog_search,RSSFeed

from django.views.generic import TemplateView
from django.contrib.auth.views import login,logout,password_change,password_change_done

def hello(request):
    #最简单的定义url例子
    return res("hello world")

admin.autodiscover()
   
urlpatterns = [
    #(不开启的app要注释掉url以提升性能)
    url(r'^admin/', admin.site.urls),
    url(r'^hello/',hello),

    url(r'^blog/$',blog_list,name='blog'),
    url(r'^blog/id=(?P<id>\d+)/$',detail,name='detail'),
    url(r'^blog/category=(?P<category>\w+)/$', search_tag, name='search_tag'),
    url(r'^blog/archives/$',archives,name='archive'),
    url(r'^blog/search/$',blog_search,name='search'),
    url(r'^blog/feed/$',RSSFeed(),name='RSS'),

    url(r'^main/$', main,name='mainMsgBoard'),
    url(r'^main/guest/$', login,{'template_name':'login.html'}),
    url(r'^main/register/$', register_page,name='Register'),
    url(r'^main/register/success/$',TemplateView.as_view(template_name = 'register_success.html')),#redirect    
    url(r'^accounts/login/$',login,{'template_name':'login.html'}),#要手动加上template_name登录后跳转到main/
    url(r'^main/logout/$',logout,{'next_page':'/main/'}),
    url(r'^main/post/$',msg_post_page),
    url(r'^main/password/reset/$',register_page,name='Register_again'),

    url(r'^list/$',event_list_page,name='list'),
    url(r'^list/post$',event_post_page,name='post'),   
]
