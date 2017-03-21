from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import UserProfile
from django.contrib.auth import authenticate
from django.shortcuts import get_list_or_404, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.http import QueryDict
from django.contrib.auth import login as auth_login

def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)

def alldogs(request):
    return render(request, 'alldogs.html', [])
def survey(request):
    return render (request, 'survey.html', [])

def contact(request):
    return render (request, 'contact.html', [])

def register(request):
    return render (request, 'register.html', [])

def authlogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
    #else:
        #add pop up

    return render(request, 'login.html', {'user':user})

def matches(request):
    #get the user instance of the currently logged in user
    user=request.user

    #get the survey information from ajax POST
    #setup the userprofile instance
    userprofile=UserProfile()
    userprofile.user = user
    userprofile.grooming=request.POST.get('grooming', False)
    userprofile.dogsize=request.POST.get('dogsize', False)
    userprofile.exercise=request.POST.get('exercise', False)
    userprofile.family=request.POST.get('family', False)
    userprofile.beingalone=request.POST.get('beingalone', False)
    userprofile.homesize=request.POST.get('homesize', False)

    print userprofile.grooming
    return render(request, 'matches.html', {'userprofile': userprofile})

def registered(request):
    registered = False

    print(request.method)


    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_repeat = request.POST.get('password_repeat')

    user = User.objects.create_user(username=username, email=email, password=password)



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
