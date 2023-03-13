from rest_framework.serializers import ModelSerializer
from productos.models import Producto
from productos.models import ProductoDetalles

class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id','nombre']
