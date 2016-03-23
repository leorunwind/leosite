from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from blog.models import MessagePost
from django.template import RequestContext
from django.http import Http404
from markdown import markdown
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def my_paginator(request,posts,num):
    #自定义分页函数，提高可复用性
    paginator = Paginator(posts, num) #每页显示num个
    page = request.GET.get('page')
    
    try :
        post_list = paginator.page(page)
    except PageNotAnInteger :
        post_list = paginator.page(1)
    except EmptyPage :
        post_list = paginator.paginator(paginator.num_pages)
    return post_list
    
# Create your views here.
def blog_list(request):
    try:
        posts = MessagePost.objects.all()
        post_list = my_paginator(request,posts,2)
        user = request.user#得到请求该页面时的用户名，判断是游客还是用户
    except MessagePost.DoesNotExist:
        raise Http404
    return render_to_response("blog.html",{'posts':post_list,'user':user},context_instance=RequestContext(request))
    
def detail(request,id = ''):
    try:
        post = MessagePost.objects.get(id = str(id))
        post.content = markdown(post.content,['codehilite'])
        post.save()
        
    except MessagePost.DoesNotExist:
        raise Http404
    return render_to_response("blogdetail.html",{'post':post},context_instance=RequestContext(request))

def archives(request):
    try:
        posts = MessagePost.objects.all()
        post_list = my_paginator(request,posts,3)
    except MessagePost.DoesNotExist:
        raise Http404
    return render_to_response("blog_archives.html",{'posts':post_list},context_instance=RequestContext(request))
    
def search_tag(request,category):
    try:
        posts = MessagePost.objects.filter(category__iexact = category) #大小写不敏感
        post_list = my_paginator(request,posts,8)#每页显示8篇
    except MessagePost.DoesNotExist :
        raise Http404
    return render_to_response("blog_archives.html",{'posts':post_list,'error':False},context_instance=RequestContext(request))  

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return HttpResponseRedirect('/blog')
        else:
            post_list = MessagePost.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render_to_response('blog_archives.html',{'posts':post_list,'error':True},
                                          context_instance=RequestContext(request))
            else :
                return render_to_response('blog_archives.html',{'posts':post_list,'error':False},
                                          context_instance=RequestContext(request))
    return HttpResponseRedirect('/')
    
class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return MessagePost.objects.order_by('-pubtime')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pubtime

    def item_description(self, item):
        return item.content