
from django.conf.urls import url
from . import views

app_name = 'dashboard'

urlpatterns = [
    url(r'^data$',
        views.order_data,
        name='coffee_data')
]
