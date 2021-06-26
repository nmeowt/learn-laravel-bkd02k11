from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
from django.shortcuts import render
from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

admin.site.site_header = "Chạn quản trị"
admin.site.site_title = "Chạn cafe"
admin.site.index_title = "Chạn cafe"
admin.site.unregister(Group)


class DashboardModel(models.Model):

    class Meta:
        verbose_name_plural = 'Xem'
        app_label = 'dashboard'


@staff_member_required
def dashboard_view(request):
    return render(request, 'dashboard/detail.html')


class DashboardModelAdmin(admin.ModelAdmin):
    model = DashboardModel

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(
            self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', dashboard_view, name=view_name),
        ]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(DashboardModel, DashboardModelAdmin)
