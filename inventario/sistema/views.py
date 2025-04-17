from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Compra, Venta

def index(request):
    return render(request, 'index.html')

def usuarios(request):
    return render(request, 'usuarios.html')

def registrar_compra(request):
    if request.method == 'POST':
        producto = request.POST['producto']
        cantidad = int(request.POST['cantidad'])
        total = float(request.POST['total'])
        fecha = timezone.now()

        Compra.objects.create(producto=producto, cantidad=cantidad, total=total, fecha=fecha)
        return redirect('vista_inventario')
    
def registrar_venta(request):
    if request.method == 'POST':
        producto = request.POST['producto']
        cantidad = int(request.POST['cantidad'])
        total = float(request.POST['total'])
        fecha = timezone.now()

        Venta.objects.create(producto=producto, cantidad=cantidad, total=total, fecha=fecha)
        return redirect('vista_inventario')
    
def vista_inventario(request):
    compras = Compra.objects.all().order_by('-fecha')
    return render(request, 'compras.html', {'compras': compras})

def stock_view(request):
    return render(request, 'stock.html')

def ventas_view(request):
    return render(request, 'ventas.html')

def compras_view(request):
    return render(request, 'compras.html')
