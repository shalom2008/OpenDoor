from django.db import models
from datetime import datetime
from OpenDoor.settings import document_status

from apps.base_data.models import Customer, Brand
# Create your models here.


class OrderHeader(models.Model):
    order_name = models.CharField(max_length=14, unique=True, verbose_name='')
    date = models.DateField(verbose_name='', default=datetime.now)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              limit_choices_to={'is_active': True})
    status = models.CharField(max_length=1, verbose_name='', choices=document_status)