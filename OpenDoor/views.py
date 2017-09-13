from django.shortcuts import render
from . import settings


def index(request):
    context = settings.INSTALLED_APPS[6:]
    return render(request, 'index.html', {"index": context})
