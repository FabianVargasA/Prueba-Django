from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion =models.TextField()
    precio =models.DecimalField(max_digits=10,decimal_places=2)

    

class ProductoDetalles(models.Model):
    idProducto =  models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()  
    valorTotal = models.DecimalField(max_digits=100,decimal_places=2)
    valorIva = models.DecimalField(max_digits=10,decimal_places=2)

    

    