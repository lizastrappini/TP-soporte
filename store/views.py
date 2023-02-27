from django.shortcuts import render, HttpResponse, redirect
from .models import Producto, Categoria, Carrito
from cuentas.models import CustomUser
from django.contrib import messages
# Create your views here.

def storeView(request):
    productos = Producto.objects.all()
    categorias =  Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias': categorias, 
    }
    return render(request, 'store/store.html', context)

def checkout(request):
    carrito = Carrito(request)
    user = request.user
    context = {
        'carrito': carrito,
        'user': user,
    }
    return render(request, 'store/checkout.html' , context)

def agregarProductoView(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    talle = request.GET['talle']
    if producto.stock >= 1:
        carrito.agregar(producto, talle)
    else:
        messages.warning(request, 'No hay stock suficiente para agregar una unidad mas')
    return redirect("home")

def eliminarProductoView(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("home")

def limpiarCarritoView(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("home")

def getBy_Categoria(request, categ_id):
    productos = Producto.getBy_Categoria(categ_id)
    categorias =  Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias' : categorias,
    }
    return render(request, 'store/store.html', context)

def getBy_Sexo(request, sexo):
    productos = Producto.getBy_Sexo(sexo)
    categorias =  Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias' : categorias,
    }
    return render(request, 'store/store.html', context)

def getBy_Marca(request, marcaProd):
    productos = Producto.getBy_Marca(marcaProd)
    categorias =  Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias' : categorias,
    }
    return render(request, 'store/store.html', context)

def getBy_Envio(request, envio):
    productos = Producto.getBy_EnvioGratis(envio)
    categorias =  Categoria.objects.all()
    context = {
        'productos': productos,
        'categorias' : categorias,
    }
    return render(request, 'store/store.html', context)
