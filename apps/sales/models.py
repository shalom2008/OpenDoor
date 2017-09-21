from django.db import models
from datetime import datetime
from OpenDoor.settings import document_status

from apps.basedata.models import BaseItem, Customer, Brand, Staff, Department,\
    Material, Currency, Tax
# Create your models here.


class OrderParm(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='')
    parm_type = models.CharField(max_length=32, choices=(('manual', '手工录入'),
                                                         ('relate_item', '关联项目')),
                                 verbose_name='')
    relate_item = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                    limit_choices_to={'is_active': True})
    parm_class = models.CharField(max_length=16, choices=(('char', '字符串'),
                                                          ('int', '整数'),
                                                          ('float', '小数')))
    parm_len = models.IntegerField(verbose_name='', default=32)

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class SaleType(models.Model):
    name = models.CharField(max_length=16, verbose_name='', unique=True)
    desc = models.CharField(max_length=128, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class InvoiceHeader(models.Model):
    invoice_name = models.CharField(max_length=14, unique=True, verbose_name='')
    date = models.DateField(verbose_name='', default=datetime.now)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              limit_choices_to={'is_active': True})
    status = models.CharField(max_length=1, verbose_name='', choices=document_status)
    sale_type = models.ForeignKey(SaleType, on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    salesman = models.ForeignKey(Staff, related_name='inv_salesman', on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    order_taker = models.ForeignKey(Staff, related_name='inv_order_taker', on_delete=models.PROTECT,
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

    def __str__(self):
        return self.invoice_name


class InvoiceDetail(models.Model):
    invoice_pk = models.ForeignKey(InvoiceHeader, on_delete=models.PROTECT)
    material = models.ForeignKey(Material, on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})