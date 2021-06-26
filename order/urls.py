from . import views
from django.conf.urls import url

app_name = 'order'

urlpatterns = [
    url(r'^create/$',
        views.order_create,
        name='create'),
]
