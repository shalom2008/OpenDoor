from django.db import models

# Create your models here.


class BaseItem(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='项目名称')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '基础资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Department(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=32, unique=True, verbose_name='部门名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '部门'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Staff(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=32, unique=True, verbose_name='职员名称')
    department = models.ForeignKey(Department, on_delete=models.PROTECT,
                                   limit_choices_to={'is_active': True})
    desc = models.CharField(max_length=128, unique=True, verbose_name='备注')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '职员'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CustomerType(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=24, unique=True, verbose_name='客户类别名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '客户类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Brand(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=24, unique=True, verbose_name='品牌名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    img = models.ImageField(verbose_name='品牌图片')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '经营品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Customer(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=64, verbose_name='客户简称', unique=True)
    fullname = models.CharField(max_length=128, verbose_name='客户全称', unique=True)
    phone = models.CharField(max_length=11, verbose_name='手机')
    address = models.CharField(max_length=256, verbose_name='地址')
    brand = models.ManyToManyField(Brand, related_name='customer_brand',
                                   limit_choices_to={'is_active': True})
    we_chat = models.CharField(max_length=32, verbose_name='微信号', blank=True)
    contact_man = models.CharField(max_length=32, verbose_name='联系人')
    contact_number = models.CharField(max_length=64, verbose_name='联系电话')
    fax_number = models.CharField(max_length=64, verbose_name='传真号码')
    type = models.ForeignKey(CustomerType, on_delete=models.PROTECT,
                             limit_choices_to={'is_active': True})
    is_active = models.BooleanField(default=True, verbose_name='有效')
    salesman = models.ForeignKey(Staff, related_name='cus_salesman', on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    order_taker = models.ForeignKey(Staff, related_name='cus_order_taker', on_delete=models.PROTECT,
                                    limit_choices_to={'is_active': True})
    credit_limit = models.BooleanField(default=False, verbose_name='信用检查')
    credit = models.DecimalField(verbose_name='信用额度', blank=True, decimal_places=3, max_digits=15)
    desc = models.TextField(verbose_name='备注', blank=True)

    class Meta:
        verbose_name = '客户资料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Series(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=32, unique=True, verbose_name='系列名称')
    desc = models.CharField(max_length=128, verbose_name='备注')
    is_active = models.BooleanField(default=True, verbose_name='有效')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              limit_choices_to={'is_active': True})

    class Meta:
        verbose_name = '产品系列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Color(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=32, unique=True, verbose_name='颜色名称')
    img = models.ImageField(verbose_name='颜色图片')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '颜色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MaterialType(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=16, unique=True, verbose_name='物料类别名称')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '物料类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class MaterialOrigin(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=16, unique=True, verbose_name='物料来源名称')
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '物料来源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Unit(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=16, verbose_name='单位名称', unique=True)
    symbol = models.CharField(max_length=16, verbose_name='单位符号', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '单位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Material(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    encoder = models.CharField(max_length=32, verbose_name='物料编码')
    name = models.CharField(max_length=64, unique=True, verbose_name='物料名称')
    specification = models.CharField(max_length=64, verbose_name='规格')
    series = models.ForeignKey(Series, on_delete=models.PROTECT,
                               limit_choices_to={'is_active': True})
    type = models.ForeignKey(MaterialType, on_delete=models.PROTECT,
                             limit_choices_to={'is_active': True})
    origin = models.ForeignKey(MaterialOrigin, on_delete=models.PROTECT,
                               limit_choices_to={'is_active': True})
    main_unit = models.ForeignKey(Unit, related_name='main_unit', on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    aux_unit = models.ForeignKey(Unit, related_name='aux_unit', on_delete=models.PROTECT,
                                 limit_choices_to={'is_active': True})
    sale_unit = models.ForeignKey(Unit, related_name='sale_unit', on_delete=models.PROTECT,
                                  limit_choices_to={'is_active': True})
    stock_unit = models.ForeignKey(Unit, related_name='stock_unit', on_delete=models.PROTECT,
                                   limit_choices_to={'is_active': True})
    purchase_unit = models.ForeignKey(Unit, related_name='purchase_unit', on_delete=models.PROTECT,
                                      limit_choices_to={'is_active': True})
    produce_unit = models.ForeignKey(Unit, related_name='produce_unit', on_delete=models.PROTECT,
                                     limit_choices_to={'is_active': True})
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '物料'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Currency(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=16, verbose_name='币别名称', unique=True)
    symbol = models.CharField(max_length=16, verbose_name='货币符号', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '币种'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tax(models.Model):
    item_id = models.ForeignKey(BaseItem, on_delete=models.PROTECT,
                                limit_choices_to={'is_active': True})
    name = models.CharField(max_length=16, verbose_name='税别名称', unique=True)
    tax_rate = models.FloatField(verbose_name='税率', unique=True)
    is_active = models.BooleanField(default=True, verbose_name='有效')

    class Meta:
        verbose_name = '税种'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
