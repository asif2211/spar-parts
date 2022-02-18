from django.contrib import admin

from .models import Product, Item, Sale

admin.site.register(Product)
admin.site.register(Item)
admin.site.register(Sale)
