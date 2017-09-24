from django.contrib import admin

from .models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    fields = ['we_chat', 'name', 'fullname', 'phone', 'address', 'contact_man', 'fax_number'
              , 'credit_limit', 'order_taker']


admin.site.register(Customer, CustomerAdmin)
