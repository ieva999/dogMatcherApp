from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from app.models import UserProfile
from django.contrib.auth import authenticate


def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)

def surveyinput(request):

    userprofile=request.user.get_profile()
    #userprofile.beingalone=
    #userprofile.dogsize=
    #userprofile.exercise=
    userprofile.family=request.POST.get('family')
    #userprofile.grooming=
    #userprofile.homesize=



def register(request):
    registered = False

    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password_repeat = request.POST.get('password_repeat')
    user=User()
    user = User.objects.create_user(username, email, password)
    user.save()

    userprofile=UserProfile()
    userprofile.user=user
    userprofile.save(commit=False)

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
