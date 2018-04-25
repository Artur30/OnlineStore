from django.conf.urls import url
from . import views


app_name = 'store'

urlpatterns = [
    url(r'^(?P<id>\d+)/(?P<product_slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<category_slug>[-\w]+)', views.product_list, name='product_list_by_category'),
    url(r'^$', views.product_list, name='product_list'),

]
