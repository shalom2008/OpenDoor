from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=24, verbose_name='经营品牌')
    desc = models.CharField(max_length=140, verbose_name='备注')
    img = models.ImageField(verbose_name='品牌图标')

    class Meta:
        verbose_name = '客户品牌'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
