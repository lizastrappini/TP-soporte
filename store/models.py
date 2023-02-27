from django.db import models
from django.contrib import messages
# Create your models here.

class Categoria(models.Model):

    nombre = models.CharField(
        max_length=40, 
        unique=True,
    )

class Producto(models.Model):

    sexo_choices = [
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('U', 'Unisex'),
    ]

    unidad_talle_choices = [
        ('N', 'Numeros'),
        ('L', 'Letras'),
    ]

    nombre = models.CharField(
        max_length=40,
    )

    precio = models.FloatField()

    imagen = models.ImageField()

    stock = models.IntegerField()

    envio_gratis = models.BooleanField(
        default=False,
    )

    sexo = models.CharField(
        max_length=1, 
        choices=sexo_choices,
    )

    marca = models.CharField(
        max_length=40,
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
    )

    unidad_talle = models.CharField(
        max_length=1, 
        choices=unidad_talle_choices,
    )

    def getBy_Categoria(categ_id):
        productos = Producto.objects.filter(categoria=categ_id)
        return productos
    
    def getBy_Sexo(sexo):
        productos = Producto.objects.filter(sexo=sexo)
        return productos

    def getBy_EnvioGratis(envio):
        productos = Producto.objects.filter(envio_gratis=envio)
        return productos
    
    def getBy_Marca(marca):
        productos = Producto.objects.filter(marcaProd=marca)
        return productos
    
    def getBy_Id(idProd):
        productos = Producto.objects.filter(id=idProd)
        return productos

    def getBy_Name(nombreProd):
        productos = Producto.objects.filter(nombre__icontains='nombreProd')
        return productos

class Carrito:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto, talle):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio" : producto.precio,
                "acumulado": producto.precio,
                "imagen" : producto.imagen.url,
                "talle": talle,
                "stock" : producto.stock,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
            self.carrito[id]["talle"] += f", {talle}"
        producto.stock -= 1
        producto.save()
        self.guardarCarrito()
            
    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
    
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            cantidad = self.carrito[id]["cantidad"]
            producto.stock += cantidad
            del self.carrito[id]
            producto.save()
            self.guardarCarrito()

    def restar(self, producto):
        id = str(producto.id) 
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            producto.stock += 1
            if self.carrito[id]["cantidad"] == 0:
                del self.carrito[id]
            producto.save()
            self.guardarCarrito()  

    def limpiar(self):  
        for id in self.carrito.keys():
            producto = Producto.getBy_Id(id)[0]
            producto.stock += self.carrito[id]["cantidad"]
            producto.save()
        self.session["carrito"] = {}
        self.session.modified = True
