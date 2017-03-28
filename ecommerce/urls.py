from django.conf.urls import url

from . import views

app_name = 'ecommerce'
urlpatterns = [
    url(r'^detail/(?P<product_id>\d+)/$', views.product_detail, name='product_detail'),
    url(r'^checkout/(?P<product_id>\d+)/$', views.checkout, name='checkout'),
    url(r'^register/$', views.register_page, name='register_page'),
    url(r'^user_profile/$', views.user_profile, name='user_profile'),
    url(r'^login/$', views.login_ecommerce, name='login_ecommerce'),
    url(r'^logout/$', views.logout_ecommerce, name='logout_ecommerce'),
    url(r'^dashboard/$', views.dashboard_ecommerce, name='dashboard_ecommerce'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^$', views.home_ecommerce, name='home_ecommerce'),
]
