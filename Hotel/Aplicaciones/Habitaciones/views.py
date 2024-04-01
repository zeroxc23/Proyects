from django.shortcuts import render, redirect
from . models import Habitaciones, tipoHabitaciones
from django.contrib import messages

def home(request):
    habitacion=Habitaciones.objects.all()
    messages.success(request,'Habitaciones Listadas')
    tipohab = tipoHabitaciones.objects.all()
    return render(request,"Admin_Hab.html",{"habitacion":habitacion, "tipohab": tipohab})


def registroHab(request):
    if request.method == 'POST':
        id_tipo_hab_id = int(request.POST.get('txtTipo'))
        estado = request.POST.get('txtEstado')

        tipo_habitacion = tipoHabitaciones.objects.get(pk=id_tipo_hab_id)

        habitacion = Habitaciones.objects.create(
            id_tipo_hab=tipo_habitacion, estado=estado
        )
    messages.success(request,'Habitación Registrada')
    return redirect('IndexHab')


def edicionHab(request, Id_habitacion):
    habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
    tipohab = tipoHabitaciones.objects.all()
    return render(request, "editarHab.html", {"habitacion":habitacion, "tipohab": tipohab})


def editarHab(request):
    if request.method == 'POST':
        Id_habitacion=request.POST['txtIdHab']
        id_tipo_hab=request.POST['txtTipo']
        estado=request.POST['txtEstado']
        
        tipo_habitacion = tipoHabitaciones.objects.get(pk=id_tipo_hab)

        habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
        habitacion.id_tipo_hab = tipo_habitacion
        habitacion.estado = estado
        habitacion.save()
    
        messages.success(request,'Habitación Actualizada')
        
        return redirect("registroHab")

def eliminarHab(request, Id_habitacion):
    habitacion = Habitaciones.objects.get(Id_habitacion=Id_habitacion)
    habitacion.delete()

    messages.success(request,'Habitación Eliminada')

    return redirect('IndexHab')

