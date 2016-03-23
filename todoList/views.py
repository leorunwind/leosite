from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from todoList.models import EventPost
from todoList.forms import EventPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def event_list_page(request):
    posts = EventPost.objects.all()
    return render_to_response("event_list/main.html",{'posts':posts},context_instance=RequestContext(request))

def event_post_page(request):
    if request.method == 'POST':
        post = EventPostForm(request.POST)
        if post.is_valid():
            newmessage = EventPost(title=post.cleaned_data['title'],
                                 detail=post.cleaned_data['detail'],
                                 #user=request.user,
                                 )
            newmessage.save()
        return HttpResponseRedirect('/list/')
    else:
        post = EventPostForm()
        
    return render_to_response("event_list/event_post_page.html",{'posts':post},context_instance=RequestContext(request))