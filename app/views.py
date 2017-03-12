from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import UserManager
from django.contrib.auth import authenticate


def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)

def register(request):
    registered = False

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_repeat = request.POST.get('password_repeat')
    print('\n\n\n'+username+'\n\n\n')
    user=User()
    user = User.objects.create_user(username, email, password)
    user.save()



    return render(request,
                'index.html',
                {
                #'profile_form': profile_form,
                'registered': registered})

def authenticateuser(request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        userbool=authenticate(username=username, password=password)

        if userbool is not None:
            login(request,userbool)
            return render(request, 'survey.html', {})
        else:
            return render(request, 'index.html', {})
            #add popup later with error (couldnt log in)
