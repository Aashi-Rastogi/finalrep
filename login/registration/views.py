from django.shortcuts import render_to_response
from django.template import RequestContext
from registration.models import loginn
import datetime

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']

       post = loginn(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()

    # Get all posts from DB
    posts = loginn.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = loginn.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': loginn.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = loginn.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': loginn.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))