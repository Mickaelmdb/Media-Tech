from django.contrib import admin
from .models import Category, Product

#Cette classe permet d' enregistrer les models dans la console d'administration 

#Permets de gérer les catégories depuis la console d'admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

#Permets de gérer les produits depuis la console d'admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price',
                    'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}