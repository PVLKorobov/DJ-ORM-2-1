from django.contrib import admin

from .models import Product, Order, OrderPosition

# Register your models here.


class OrderPosInline(admin.TabularInline):
    model = OrderPosition
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price']
    list_filter = ['category']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id']
    inlines = [OrderPosInline]


@admin.register(OrderPosition)
class OrderPosAdmin(admin.ModelAdmin):
    pass