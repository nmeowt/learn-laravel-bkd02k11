
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView


app_name = 'account'

urlpatterns = [
    url(r'login',
        LoginView.as_view(template_name='account/login.html'),
        name='login'
        ),
    url(r'^logout$',
        views.logout,
        name='logout'),
    url(r'^name$',
        views.get_name,
        name='get-name',
        ),
]
