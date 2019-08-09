# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Name


@admin.register(Name)
class NameAdmin(admin.ModelAdmin):
    pass
