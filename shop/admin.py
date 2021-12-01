from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}
    ordering=('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','price','description','image','offer','ratings','in_stock','is_new']
    list_editable=['price','image','offer','in_stock','is_new']
    prepopulated_fields={'slug':('name',)}
    ordering=('name',)
    
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}
    ordering=('name',)

@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display=['name']
    prepopulated_fields={'slug':('name',)}
    ordering=('name',)
    
