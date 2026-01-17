from django.contrib import admin

# Register your models here.
from .models import Order, Product

admin.site.site_header = "E-Commerce Admin"
admin.site.site_title = "E-Commerce Admin Portal"
admin.site.index_title = "Welcome to E-Commerce Admin Portal"

class ProductAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = "Change category to default"

    list_display = ('title', 'price', 'discount_price', 'category', 'description')
    search_fields = ('title', 'category')
    actions = [change_category_to_default]
    fields = ('title', 'price')
    list_editable = ('discount_price', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
