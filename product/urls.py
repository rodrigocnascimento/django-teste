from django.conf.urls import url

from . import views

app_name = 'product'
urlpatterns = [
    url(r'^product/add/$', views.add, name='add'),
    url(r'^product/edit/(?P<product_id>\d+)/$', views.edit, name='edit'),
    url(r'^product/delete/(?P<product_id>\d+)/$', views.delete, name='delete'),
    url(r'^product/$', views.index, name='index'),
]
