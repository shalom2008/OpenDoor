import xadmin

from .models import Department


class DepartmentAdmin(object):
    list_display = []


xadmin.site.register(Department, DepartmentAdmin)
