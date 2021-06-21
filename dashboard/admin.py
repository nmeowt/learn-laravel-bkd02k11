from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.site_header = "Chạn quản trị"
admin.site.site_title = "Chạn cafe"
admin.site.index_title = "Chạn cafe"
admin.site.unregister(Group)
