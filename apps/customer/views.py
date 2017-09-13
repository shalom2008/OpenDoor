from django.shortcuts import render

from .models import Customer

# Create your views here.


def index(request):
    customer_list = Customer.objects.get()[:5]
    context = {'customer_list': customer_list}

    return render(request, 'customer/index.html', context)
