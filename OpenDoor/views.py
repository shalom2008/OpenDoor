from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import settings


def index(request):
    context = settings.INSTALLED_APPS[6:]
    return render(request, 'index.html', {"index": context})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'login.html')
