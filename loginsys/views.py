from django.shortcuts import render, render_to_response, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User


def login(request):
    args = {}
    args.update(csrf(request))
    
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('login.html', args)

    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect("/")




def register(request):
    args = {} 
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 == password2:
            user = User.objects.create_user(username, email, password1)

            user.save()
            return render_to_response('login.html', args)
        else:
            args['login_error'] = "Пароли не совпадают! Попробуйте еще раз!"
            return render_to_response('register.html', args)
    else:
        return render_to_response('register.html', args)