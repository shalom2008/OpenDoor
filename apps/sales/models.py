from django.db import models
from datetime import datetime
from OpenDoor.settings import document_status

from apps.basedata.models import BaseItem, Customer, Brand, Staff, Department,\
    Material, Currency, Tax, SaleType
from common.generic import BaseOrderObject
# Create your models here.


class InvoiceHeader(BaseOrderObject):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              limit_choices_to={'is_active': True})
    sale_type = models.ForeignKey(SaleType, on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    salesman = models.ForeignKey(Staff, related_name='invoice_salesman', on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    order_taker = models.ForeignKey(Staff, related_name='invoice_order_taker', on_delete=models.PROTECT,
                                    limit_choices_to={'is_active': True})
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   limit_choices_to={'is_active': True})
    address = models.CharField(max_length=256, verbose_name='地址')
    fax_number = models.CharField(max_length=64, verbose_name='传真号码')
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT,
                            limit_choices_to={'is_active': True})

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name


class InvoiceDetail(models.Model):
    invoice_pk = models.ForeignKey(InvoiceHeader, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    invoice_qty = models.DecimalField(verbose_name='', max_digits=15, decimal_places=3)
    delivery_date = models.DateField(verbose_name='', blank=True, null=True)
    price = models.DecimalField(verbose_name='', max_digits=15, decimal_places=3)
    discount = models.DecimalField(verbose_name='', max_digits=15, decimal_places=3)
    amount = models.DecimalField(verbose_name='', max_digits=15, decimal_places=3)

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return ''