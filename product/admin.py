from django.contrib import admin
from product.models import Product, Sale


class ProductAdmin(admin.ModelAdmin):
    list_display = ('user_fullname', 'product_name', 'product_qtd', 'product_price', 'pub_date')
    search_fields = ['product_name']
    list_filter = ['pub_date']


class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'product', 'seller_fullname', 'buyer_fullname', 'sale_product_qtd', 'sale_product_price',
        'total_sale', 'sale_date')


admin.site.register(Product, ProductAdmin)
admin.site.register(Sale, SaleAdmin)
