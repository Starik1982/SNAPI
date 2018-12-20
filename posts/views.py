from django.shortcuts import (
    render,
    render_to_response,
    redirect,
    get_object_or_404,
)
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate

from django.contrib import messages

from .models import *
from .forms import PostForm

def info(request):
    return render_to_response('info.html')

def get_post(request, post_id=1):
    args = {}
    args['get_post'] = Post.objects.get(id=post_id)
    return render_to_response('get_post.html', args)


def post_list(request):
    args = {}
    args['posts'] = Post.objects.order_by('-id')
    return render_to_response('post_list.html', args)


def post_create(request):
    if  not request.user.username:
         response = HttpResponse("Только зарегистрированые пользователи могу добавлять публикации.")
         return response
    if request.POST:
        user = request.user
        title =  request.POST.get('title', '')
        content = request.POST.get('content', '')
        q = Post(user = user, title = title, content = content)
        q.save()    #
        return redirect('/')

    return render(request, "post_create.html")


def post_update(request, id=None):
    instance = Post.objects.get(id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/')

    context = {
        'title': instance.title,
        'content': instance.content,
        'form':form,
    }
    return render(request, "post_edit.html", context)



def post_delete(request, post_id=None):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = Post.objects.get(id=post_id)
    instance.delete()
    return redirect("/")


def ad_like(request, post_id = 1):    
    instance = Post.objects.get(id=post_id)
    user = request.user.id
    user_who_like_id = instance.like_id.split()
    user_who_dislike_id = instance.dislike_id.split()
    if not str(user) in user_who_like_id:
        print(user_who_like_id)
        instance.like = instance.like + 1
        instance.like_id = instance.like_id +' '+ str(user)
        print(instance.like_id)
        
        if str(user) in user_who_dislike_id:
            user_who_dislike_id.remove(str(user))
            s =" " 
            instance.dislike_id = s.join(user_who_dislike_id)
            instance.dislike = instance.dislike - 1            
            print(instance.like_id)
        instance.save()
    return redirect("/")




def ad_dislike(request, post_id = 1):
    instance = Post.objects.get(id=post_id)
    user = request.user.id
    user_who_like_id = instance.like_id.split()
    user_who_dislike_id = instance.dislike_id.split()
    if not str(user) in user_who_dislike_id:
        instance.dislike = instance.dislike + 1
        instance.dislike_id = instance.dislike_id +' '+ str(user)
        
        if str(user) in user_who_like_id:
            user_who_like_id.remove(str(user))
            s =" " 
            instance.like_id = s.join(user_who_like_id)
            instance.like = instance.like - 1            
        instance.save()
    return redirect("/")





