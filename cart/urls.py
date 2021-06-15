from django.conf.urls import url

from . import views

app_name = 'cart'

urlpatterns = [
    url(r'^$', views.cart_detail,
        name='cart-detail'),
    url(r'^add$',
        views.cart_add,
        name='cart-add'),
    url(r'^remove/(?P<product_id>\d+)/$',
        views.cart_remove,
        name='cart-remove'),
    url(r'^total-item$',
        views.cart_total_items,
        name='cart-total-item'),
]
