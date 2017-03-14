from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import UserProfile
from django.contrib.auth import authenticate


def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)

def surveyinput(request):

    #get the user instance of the currently logged in user
    user=request.user



    #setup the userprofile instance
    userprofile=UserProfile()
    userprofile.user = user
    userprofile.grooming=request.POST.get('grooming')
    userprofile.dogsize=request.POST.get('dogsize')
    userprofile.exercise=request.POST.get('exercise')
    userprofile.family=request.POST.get('family')
    userprofile.beingalone=request.POST.get('beingalone')
    userprofile.homesize=request.POST.get('homesize')
    return render(request, 'index.html', {})

def register(request):
    registered = False

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_repeat = request.POST.get('password_repeat')
    print("\n\n\n\n"+username+"\n\n\n\n\n")
    user=User()
    user = User.objects.create_user(username, email, password)
    user.save()
    print("\n\n\n\n" + username + "\n\n\n\n\n")
    user.is_active=True
    userauth = authenticate(username=username, password=password)
    login(request, userauth)

    return render(request, 'survey.html', {'registered': registered})

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
