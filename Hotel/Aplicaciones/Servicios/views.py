from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Bar, Restaurante, ZonasHumedas

#Apartado Restaurante:

#Extracción de Datos y Vista Principal
def homeRest(request):
    producto=Restaurante.objects.all()
    messages.success(request, '¡Platillos Listados!')
    return render(request,"Admin_Rest.html",{"rest":producto})

#Resgistro Tablas
def registroRest(request):
    Id_producto=request.POST['txtId_Producto']
    TipoPlatillo=request.POST['txtTipoPlatillo']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio']
    Estado=request.POST['txtEstado']
    producto=Restaurante.objects.create(Id_producto=Id_producto, 
                           TipoPlatillo=TipoPlatillo,
                           Nombre=Nombre,
                           Precio=Precio,
                           Estado=Estado,
                           )
    messages.success(request, '¡Platillo Registrado!')
    return redirect('/IndexRest/')
#Eliminar Tabla
def eliminarRest(request,Id_producto):
    producto=Restaurante.objects.get(Id_producto=Id_producto)
    producto.delete()
    messages.success(request, '¡Platillo Eliminado!')
    
    return redirect('/IndexRest/')
#Edición Tabla
def edicionRest(request,Id_producto):
    producto=Restaurante.objects.get(Id_producto=Id_producto)
    return render(request,"editarRest.html",{'bar':producto})
    
def editarRest(request):
    Id_producto=request.POST['txtId_Producto']
    TipoPlatillo=request.POST['txtTipoPlatillo']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio'].replace(',', '.')
    Estado=request.POST['txtEstado']

    producto=Restaurante.objects.get(Id_producto=Id_producto)
    producto.TipoPlatillo=TipoPlatillo
    producto.Nombre=Nombre
    producto.Precio=Precio
    producto.Estado=Estado
    producto.save()
    messages.success(request, '¡Producto actualizado!')
    return redirect('/IndexRest/')
   
#######################################################################
#Apartado Bar:

#Extracción de Datos y Vista Principal
def homeBar(request):
    producto=Bar.objects.all()
    messages.success(request, '¡Productos listados!')
    return render(request,"Admin_bar.html",{"bar":producto})

#Resgistro Tabla
def registroBar(request):
    Id_producto=request.POST['txtId_Producto']
    TipoBebida=request.POST['txtTipoBebida']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio']
    Estado=request.POST['txtEstado']
    producto=Bar.objects.create(Id_producto=Id_producto, 
                           TipoBebida=TipoBebida,
                           Nombre=Nombre,
                           Precio=Precio,
                           Estado=Estado,
                           )
    messages.success(request, '¡Producto Registrado!')
    return redirect('/IndexBar/')

#Eliminar Tabla
def eliminarBar(request,Id_producto):
    producto=Bar.objects.get(Id_producto=Id_producto)
    producto.delete()
    messages.success(request, '¡Producto Eliminado!')
    
    return redirect('/IndexBar/')
#Edición Tabla
def edicionBar(request,Id_producto):
    producto=Bar.objects.get(Id_producto=Id_producto)
    return render(request,"editarBar.html",{'bar':producto})
    
def editarBar(request):
    Id_producto=request.POST['txtId_Producto']
    TipoBebida=request.POST['txtTipoBebida']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio'].replace(',', '.')
    Estado=request.POST['txtEstado']

    producto=Bar.objects.get(Id_producto=Id_producto)
    producto.TipoBebida=TipoBebida
    producto.Nombre=Nombre
    producto.Precio=Precio
    producto.Estado=Estado
    producto.save()
    messages.success(request, '¡Producto Actualizado!')
    return redirect('/IndexBar/')
   
#######################################################################

#Apartado Zonas Humedas:

#Extracción de Datos y Vista Principal
def homeZh(request):
    producto=ZonasHumedas.objects.all()
    messages.success(request, '¡Zonas Humedas Listadas!')
    return render(request,"Admin_Zh.html",{"zh":producto})
#Resgistro Tabla
def registroZh(request):
    Id_productoZH=request.POST['txtId_Producto']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio']
    Estado=request.POST['txtEstado']
    producto=ZonasHumedas.objects.create(Id_productoZH=Id_productoZH, 
                           Nombre=Nombre,
                           Precio=Precio,
                           Estado=Estado,
                           )
    messages.success(request, '¡Zona Humeda Registrada!')
    return redirect('/IndexZh/')
#Eliminar Tabla
def eliminarZh(request,Id_productoZH):
    producto=ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    producto.delete()
    messages.success(request, 'Zona Humeda Eliminada!')
    
    return redirect('/IndexZh/')
#Edición Tabla
def edicionZh(request,Id_productoZH):
    producto=ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    return render(request,"editarZh.html",{'zh':producto})
    
def editarZh(request):
    Id_productoZH=request.POST['txtId_Producto']
    Nombre=request.POST['txtNombre']
    Precio=request.POST['txtPrecio'].replace(',', '.')
    Estado=request.POST['txtEstado']

    producto=ZonasHumedas.objects.get(Id_productoZH=Id_productoZH)
    producto.Nombre=Nombre
    producto.Precio=Precio
    producto.Estado=Estado
    producto.save()
    messages.success(request, '¡Zona Humeda Actualizada!')
    return redirect('/IndexZh/')