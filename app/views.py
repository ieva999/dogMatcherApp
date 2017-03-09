from django.shortcuts import render
from django.http import HttpResponse
from app.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def index(request):
    context_dict={}
    return render(request, 'index.html', context=context_dict)

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        #would like to have profile maybe
        #profile_form = UserProfileForm(data=request.POST)

        #add the following condition if we include profile info
         #and profile_form.is_valid()
        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()
            #profile = profile_form.save(commit=False)
            #profile.user = user

            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            #profile.save()
            registered = True
        else:
            print(user_form.errors)#, profile_form.errors #add this argument when the profile info is included
    else:
        user_form = UserForm()
        #profile_form = UserProfileForm()

    return render(request,
                'index.html',
                {'user_form': user_form,
                #'profile_form': profile_form,
                'registered': registered})
