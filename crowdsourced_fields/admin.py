"""Admin classes for the ``django-crowdsourced-fields`` app."""
from django.contrib import admin

from crowdsourced_fields.models import (
    CrowdsourcedItem,
    CrowdsourcedItemGenericForeignKey,
)


def approve_items(modeladmin, request, queryset):
    queryset.update(is_user_generated=False)
approve_items.short_description = "Approve selected items"


class CrowdsourcedItemAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'value', 'is_user_generated', )
    list_filter = ('item_type', 'is_user_generated', )
    search_fields = ['value', ]
    actions = [approve_items]


class CrowdsourcedItemGenericForeignKeyAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'item', 'content_type', 'object_id',
                    'field_name')
    list_filter = ('item_type', 'item__is_user_generated', 'field_name')
    search_fields = ['item__value', ]
    actions = [approve_items]


admin.site.register(CrowdsourcedItem, CrowdsourcedItemAdmin)
admin.site.register(
    CrowdsourcedItemGenericForeignKey, CrowdsourcedItemGenericForeignKeyAdmin)
