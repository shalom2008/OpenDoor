from django.shortcuts import render
from django.shortcuts import get_list_or_404

from .models import Customer

# Create your views here.


def index(request):
    customer_list = get_list_or_404(Customer)[:5]

    return render(request, 'customer/index.html', {'customer_list': customer_list})
