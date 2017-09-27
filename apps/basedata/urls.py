from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_name>\w+)/$', views.item_list, name='item_list')

]
