from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import UserProfile
from django.contrib.auth import authenticate
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import QueryDict

def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)


def survey(request):
    return render (request, 'survey.html', [])

def matches(request):
    user = request.user

    #setup the userprofile instance
    userprofile=UserProfile()
    userprofile.user = user
    userprofile.grooming=request.POST.get('grooming')
    userprofile.dogsize=request.POST.get('dogsize')
    userprofile.exercise=request.POST.get('exercise')
    userprofile.family=request.POST.get('family')
    userprofile.beingalone=request.POST.get('beingalone')
    userprofile.homesize=request.POST.get('homesize')

    return render (request, 'matches.html', [])

def register(request):
    registered = False

    print(request.method)


    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_repeat = request.POST.get('password_repeat')
    user=authenticate(username=username,password=password)

    if user is not None:
        if user.is_active:
            user_created=True
        else:
            user_created=False

    else:
        user = User.objects.create_user(username=username, email=email, password=password)

    user.is_active=True
    login(request, user)

    #queryDict = QueryDict()
    #QueryDict.__setitem__(queryDict, 'user', user)
    return render(request, 'registered.html', [])


def about(request):
    return render(request, 'about.html', {})

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
