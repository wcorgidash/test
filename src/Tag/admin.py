from django.contrib import admin

# Register your models here.

from .models import FilterTag, FilterTagRelation

admin.site.register(FilterTag)
admin.site.register(FilterTagRelation)