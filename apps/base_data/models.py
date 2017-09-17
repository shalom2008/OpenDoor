from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=128, verbose_name='客户简称', unique=True)
    fullname = models.CharField(max_length=256, verbose_name='客户全称', unique=True)
    phone = models.CharField(max_length=11, verbose_name='手机')
    address = models.CharField(max_length=256, verbose_name='地址')
    brand = models.ManyToManyField(Brand, limit_choices_to={'is_active': True})
    we_chat = models.CharField(max_length=32, verbose_name='微信号', blank=True)
    contact_man = models.CharField(max_length=32, verbose_name='联系人')
    contact_number = models.CharField(max_length=64, verbose_name='联系电话')
    type = models.ForeignKey(CustomerType, models.SET_NULL, blank=True, null=True,
                             limit_choices_to={'is_active': True})
    is_active = models.BooleanField(default=True, verbose_name='有效')
    salesman = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,
                                 limit_choices_to={'is_active': True})
    order_taker = models.ForeignKey(User, models.SET_NULL, blank=True, null=True,
                                    limit_choices_to={'is_active': True})
    credit_limit = models.BooleanField(default=False, verbose_name='信用检查')
    credit = models.DecimalField(verbose_name='信用额度', blank=True)
    desc = models.TextField(verbose_name='备注', blank=True)

    class Meta:
        verbose_name = '客户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='品牌名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    img = models.ImageField(verbose_name='品牌图标')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = '经营品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CustomerType(models.Model):
    name = models.CharField(max_length=24, unique=True, verbose_name='客户类别名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = '客户类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='')
    series = models.ForeignKey(Series, limit_choices_to={'is_active': True})
    type = models.ForeignKey(MaterialType, limit_choices_to={'is_active': True})
    origin =models.ForeignKey(MaterialOrigin, limit_choices_to={'is_active': True})


    class


class Series(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='')
    desc = models.CharField(max_length=128, verbose_name='')
    is_active = models.BooleanField(default=True)
    brand = models.ForeignKey(Brand, models.SET_NULL, blank=True, null=True,
                              limit_choices_to={'is_active': True})

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MaterialOrigin(models.Model):
    name = models.CharField(max_length=16, unique=True, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=16, verbose_name='', unique=True)
    symbol = models.CharField(max_length=16, verbose_name='', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class UnitGroup(models.Model):
    name = models.CharField(max_length=16, verbose_name='', unique=True)
    main_unit = models.ForeignKey(Unit)
    aux_unit = models.ForeignKey(Unit)
    rate = models.FloatField(blank=True, verbose_name='')
    is_active = models.BooleanField(default=True, verbose_name='')

    class Meta:
        verbose_name = ''
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name