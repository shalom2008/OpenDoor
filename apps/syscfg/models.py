from django.db import models

# Create your models here.


class Module(models.Model):
    name = models.CharField(max_length=32, verbose_name='')
    parent = models.ForeignKey('self', on_delete=models.PROTECT)
    url = models.CharField(max_length=64, verbose_name='')
    status = models.BooleanField(verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

