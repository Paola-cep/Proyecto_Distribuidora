from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('inventario/', views.vista_inventario, name='vista_inventario'),
    path('registrar_compra/', views.registrar_compra, name='registrar_compra'),
    path('registrar_venta/', views.registrar_venta, name='registrar_venta'),
    path('stock/', views.stock_view, name='stock'), 
    path('ventas/', views.ventas_view, name='ventas'), 
    path('compras/', views.compras_view, name='compras'),  
]
