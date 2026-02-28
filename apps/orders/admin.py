from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'created_at')  # status olib tashlandi
    list_filter = ('created_at',)  # status olib tashlandi
    search_fields = ('user__username', 'user__email')
    ordering = ('-created_at',)
    inlines = [OrderItemInline]
    readonly_fields = ('created_at', 'total_price')