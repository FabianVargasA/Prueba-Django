from django.contrib import admin

# Register your models here.
from productos.models import Producto
from productos.models import ProductoDetalles

# Register your models here.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin): 
    list_display = ['id','nombre', 'precio']

@admin.register(ProductoDetalles)
class ProductoDetallesAdmin(admin.ModelAdmin): 
    list_display = ['id','idProducto','cantidad']