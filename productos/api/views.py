from rest_framework.viewsets import ModelViewSet
from productos.models import  Producto
from productos.api.serializers import ProductoSerializer

  
class ProductoCantidadTotal(ModelViewSet):
    serializer_class = ProductoSerializer
    queryset = Producto.objects.all()

