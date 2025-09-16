from django.contrib import admin
from .models import Product
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('sku','name','category','price','stock_qty',)#To list the fields to display in admin panel

    list_filter=('category',) #Allow admin to filter product based on category 

    search_fields = ('sku', 'name') #To allow admin search by sku and name in admin panel


