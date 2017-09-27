from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404

# Create your views here.


@login_required(login_url='/login')
def index(request):
    context = get_list_or_404(ContentType, app_label='basedata')
    return render(request, 'basedata/index.html', {'item_list': context})


@login_required(login_url='/login')
def item_list(request, item_name):
    item_type = ContentType.objects.get(app_label='basedata', model=item_name)
    item = item_type.model_class()
    content = get_list_or_404(item)[:20]
    return render(request, 'basedata/item_list.html', {'content': content})

