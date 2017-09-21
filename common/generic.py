from django.db import models

from OpenDoor.settings import document_status


class BaseObject(models.Model):
    """
    All base item object derive from this class
    """
    begin = models.DateField(verbose_name='', blank=True, null=True)
    end = models.DateField(verbose_name='', blank=True, null=True)
    creator = models.CharField(verbose_name='', max_length=32, blank=True, null=True)
    modifier = models.CharField(verbose_name='', max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='', blank=True, null=True)
    modify_time = models.DateTimeField(verbose_name='', blank=True, null=True)
    desc = models.CharField(verbose_name='', max_length=64, blank=True, null=True)
    is_active = models.BooleanField(verbose_name='', default=True)

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
    begin = models.DateField(verbose_name='', blank=True, null=True)
    end = models.DateField(verbose_name='', blank=True, null=True)
    creator = models.CharField(verbose_name='', max_length=32, blank=True, null=True)
    modifier = models.CharField(verbose_name='', max_length=32, blank=True, null=True)
    create_time = models.DateTimeField(verbose_name='', blank=True, null=True)
    modify_time = models.DateTimeField(verbose_name='', blank=True, null=True)
    status = models.CharField(max_length=1, verbose_name='', choices=document_status)

    def __str__(self):
        display = getattr(self, 'order_code', None)
        if not display:
            display = ' '
        return u'%s' % display

    class Meta:
        abstract = True
