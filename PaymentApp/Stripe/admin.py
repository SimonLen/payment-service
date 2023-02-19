from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description',)
    list_filter = ('name', 'price',)
    search_fields = ('name',)


admin.site.register(Item, ItemAdmin)
