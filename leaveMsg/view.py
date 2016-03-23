from django.shortcuts import render_to_response
from django.template import loader,Context,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from leaveMsg.models import MessagePost
from leaveMsg.forms import RegisterForm,MsgPostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def archive(request):
    #显示admin中的留言
    posts = MessagePost.objects.all()
    t =loader.get_template("archive.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
    #return render(request,"archive.html",{'posts':posts})


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
                                 
def main(request):
    posts = MessagePost.objects.all()
    post_list = my_paginator(request,posts,10)
    user = request.user#把用户也作为参量传入表单，判断是否登录
    #t =loader.get_template("main.html")
    #c = RequestContext({'posts':posts})
    #return HttpResponse(t.render(c))
    return render_to_response("main.html",{'posts':post_list,'user':user},context_instance=RequestContext(request))
    
def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username = form.cleaned_data['username'],
                                            email = form.cleaned_data['email'],
                                            password = form.cleaned_data['password1'])
            return HttpResponseRedirect('/main/register/success/')
    else:
        form = RegisterForm()
     
    #提交csrf错误，http://stackoverflow.com/questions/12174040/forbidden-403-csrf-verification-failed-request-aborted
    return render_to_response("register.html",{'form':form},context_instance=RequestContext(request))
    
@login_required
def msg_post_page(request):
    if request.method == 'POST':
        form = MsgPostForm(request.POST)
        if form.is_valid():
            newmessage = MessagePost(title=form.cleaned_data['title'],
                                 content=form.cleaned_data['content'],
                                 user=request.user,
                                 )
            newmessage.save()
        return HttpResponseRedirect('/main/')
    else:
        form = MsgPostForm()
        
    return render_to_response("msg_post_page.html",{'form':form},context_instance=RequestContext(request))