from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=128, verbose_name='客户简称')
    fullname = models.CharField(max_length=256, verbose_name='客户全称')
    phone = models.IntegerField(verbose_name='手机')
    address = models.CharField(max_length=256, verbose_name='地址')

    class Meta:
        verbose_name = '客户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
