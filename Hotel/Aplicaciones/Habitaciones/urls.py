from django.urls import path
from . import views

urlpatterns=[
    path('IndexHab/',views.home, name="IndexHab"),
    path('IndexHab/registroHab/',views.registroHab, name="registroHab"),
    path('IndexHab/edicionHab/<Id_habitacion>',views.edicionHab),
    path('IndexHab/editarHab/',views.editarHab, name="editarHab"),
    path('IndexHab/eliminacionHab/<Id_habitacion>',views.eliminarHab),
    ]