from django.contrib import admin

from . import models

# ACCOUNTS BLOCK


@admin.register(models.Obj)
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('edited_photo',)
admin.site.register(models.FaceBorder)