from django.contrib import admin

# Register your models here.

from blog.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','description','author']

admin.site.register(Product,ProductAdmin)
