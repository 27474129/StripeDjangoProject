from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price")
    list_display_links = ("id", "name", "description", "price")
    search_fields = ("id", "name", "price")


admin.site.register(Item, ItemAdmin)
