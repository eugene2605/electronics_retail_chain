from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network_links.models import Supplier, Product, NetworkLink


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'name', 'email', 'country',
                    'city', 'street', 'house_number',)
    list_display_links = ('name',)
    list_filter = ('level', 'name', 'country',)
    search_fields = ('name', 'email', 'country', 'city',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'release_date',)
    list_display_links = ('name',)
    list_filter = ('name', 'model',)
    search_fields = ('name', 'model',)


@admin.register(NetworkLink)
class NetworkLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'name', 'country', 'city', 'product', 'supplier_link', 'debt_to_supplier',
                    'time_of_creation',)
    list_filter = ('contacts__city',)
    actions = ('clear_debt',)

    def level(self, obj):
        return obj.contacts.level
    level.short_description = 'уровень сети'

    def name(self, obj):
        return obj.contacts.name
    name.short_description = 'название'

    def country(self, obj):
        return obj.contacts.country
    country.short_description = 'страна'

    def city(self, obj):
        return obj.contacts.city
    city.short_description = 'город'

    def supplier_link(self, obj):
        link = reverse("admin:network_links_supplier_change", args=[obj.id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier)
    supplier_link.short_description = 'поставщик'

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, request, queryset):
        queryset.update(debt_to_supplier=None)
