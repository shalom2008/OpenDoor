from django.shortcuts import render, get_list_or_404
from django.views import generic

from .models import BaseItem, Color

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'base_data/index.html'
    context_object_name = 'base_item_set'
    model = BaseItem


class DetailView(generic.ListView):
    model = Color
    template_name = 'base_data/detail.html'
    context_object_name = 'base_item_detail'
