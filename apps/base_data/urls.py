from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='base_item_index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='base_item_detail'),

]