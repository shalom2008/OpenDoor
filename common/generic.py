from django.db import models

from datetime import datetime

from opendoor.settings import document_status


class BaseItemObject(models.Model):
    """
    All base item object derive from this class
    """
    creator = models.CharField(verbose_name='创建人', max_length=32, blank=True, null=True)
    modifier = models.CharField(verbose_name='修改人', max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', blank=True, null=True, default=datetime.now)
    modify_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)
    desc = models.CharField(verbose_name='备注', max_length=64, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='是否有效', default=1)

    def __str__(self):
        display = getattr(self, 'name', None)
        if not display:
            display = ' '
        return u'%s' % display

    class Meta:
        abstract = True


class BaseOrderObject(models.Model):
    """
    All base order object derive from this class
    """
    order_name = models.CharField(verbose_name='单据编号', unique=True, max_length=14)
    order_date = models.DateField(verbose_name='单据日期', blank=True, null=True)
    submit_date = models.DateField(verbose_name='提交日期')
    confirm_date = models.DateField(verbose_name='审核日期')
    creator = models.CharField(verbose_name='创建人', max_length=32, blank=True, null=True)
    modifier = models.CharField(verbose_name='修改人', max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', blank=True, null=True)
    modify_time = models.DateTimeField(verbose_name='修改时间', blank=True, null=True)
    status = models.CharField(max_length=1, verbose_name='单据状态', choices=document_status)
    desc = models.CharField(max_length=128, verbose_name='备注', blank=True, null=True)

    def __str__(self):
        display = getattr(self, 'order_name', None)
        if not display:
            display = ' '
        return u'%s' % display

    class Meta:
        abstract = True
