
from django.conf.urls import url
from . import views


app_name = 'store'

urlpatterns = [
    url(r'^$', views.product_list,
        name='product-list'),
    url(r'^(?P<category_slug>[-\w]+)/$',
        views.product_list,
        name='product-list-by-category'),
]
