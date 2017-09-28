import django_tables2 as tables

from . import models


class BaseItemTable(tables.Table):
   class Meta:
        model = models.Color
        attrs = {'class': 'table table-hover'}
        sequence = ('id', 'name', 'desc', '...')
