from django.contrib.auth.models import User
from Aplicaciones.Habitaciones.models import Habitaciones
from django.db import models



class Reservacion(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Id_habitacion = models.ForeignKey(Habitaciones, on_delete=models.CASCADE)
    fechaentrada = models.DateField()
    fechasalida = models.DateField()
    cantidad_Niños = models.IntegerField()
    cantidad_Adultos = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    POR_CONFIRMAR = 'Por Confirmar'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'
    ESTADO_CHOICES = [
        (POR_CONFIRMAR, 'Por Confirmar'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada')
    ]
    
    estado = models.CharField(max_length=25, choices=ESTADO_CHOICES, default=POR_CONFIRMAR)
