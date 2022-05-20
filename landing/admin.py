from django.contrib import admin
from .models import *
from django.db import models


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'service_group')


admin.site.register(Service, ServiceAdmin)
admin.site.register(FAQ)
admin.site.register(News, NewsAdmin)
admin.site.register(PassDocs)
admin.site.register(ServiceGroup)
admin.site.register(AboutUs)
