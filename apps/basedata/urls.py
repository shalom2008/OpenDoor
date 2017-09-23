from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='base_item_index'),
    url(r'^(?P<item_name>\w+)/$', views., name='base_item_list'),

]