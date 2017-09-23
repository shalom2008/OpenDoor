from django.shortcuts import render, get_list_or_404

from .models import Item, Color

# Create your views here.


def item_list(request, item_name):

