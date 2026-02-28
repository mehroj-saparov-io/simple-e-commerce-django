from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('get_image', 'name', 'price', 'available')
    search_fields = ('name', 'description')
    list_filter = ('available', 'price')
    list_editable = ('price', 'available')
    readonly_fields = ('display_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" style="border-radius: 5px; object-fit: cover;"/>')
        return "Rasm yo'q"
    
    get_image.short_description = 'Rasm'

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="200" style="border-radius: 10px;"/>')
        return "Rasm yuklanmagan"

    display_image.short_description = 'Hozirgi rasm'
