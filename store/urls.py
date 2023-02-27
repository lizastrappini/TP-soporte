from django.urls import path

from .views import storeView, checkout, agregarProductoView, eliminarProductoView, limpiarCarritoView, getBy_Categoria, getBy_Sexo,getBy_Envio


urlpatterns = [
    path('', storeView, name='home'),
    path('checkout/', checkout, name='checkout'),
    path('agregar/<int:producto_id>/', agregarProductoView, name="agregarProducto"),
    path('eliminar/<int:producto_id>/', eliminarProductoView, name="eliminarProducto"),
    path('limpiar/', limpiarCarritoView, name="limpiarCarrito"),
    path('categoria/<int:categ_id>', getBy_Categoria, name="filtro"),
    path('sexo/<str:sexo>', getBy_Sexo, name="filtroS"),
    path('envio/<str:envio>', getBy_Envio, name="filtroEnvio"),
]