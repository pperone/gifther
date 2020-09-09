from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'woman', 'occasion', 'link', 'votes', 'price')
    list_editable = ('votes',)
