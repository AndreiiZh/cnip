from django.contrib import admin
from django.contrib.gis.db import models
from django.urls import reverse
from mapwidgets.widgets import GooglePointFieldWidget

from .models import User, Question, Service, ListService


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service', 'slug']
    prepopulated_fields = {'slug': ('service',)}


class ListServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_display_links = ('title', 'price')
    search_fields = ['category__service', 'title']
    list_filter = ['category']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(User)
admin.site.register(Question)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ListService, ListServiceAdmin)
