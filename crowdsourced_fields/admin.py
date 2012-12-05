"""Admin classes for the ``django-crowdsourced-fields`` app."""
from django.contrib import admin

from crowdsourced_fields.models import (
    CrowdsourcedItem,
    CrowdsourcedItemGenericForeignKey,
)


class CrowdsourcedItemAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'value', 'is_user_generated', )
    list_filter = ('item_type', 'is_user_generated', )
    search_fields = ['value', ]


admin.site.register(CrowdsourcedItem, CrowdsourcedItemAdmin)
