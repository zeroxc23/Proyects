from django.urls import path
from . import views

urlpatterns = [
    #Bar Urls
    path('IndexBar/', views.homeBar,name="IndexBar"),
    path('IndexBar/registroBar/', views.registroBar,name='registroBar'),
    path('IndexBar/edicionBar/<Id_producto>',views.edicionBar),
    path('IndexBar/eliminarBar/<Id_producto>',views.eliminarBar),
    path('IndexBar/editarBar/',views.editarBar,name='editarBar'),
    #Restaurante Urls
    path('IndexRest/', views.homeRest,name="IndexRest"),
    path('IndexRest/registroRest/', views.registroRest,name='registroRest'),
    path('IndexRest/edicionRest/<Id_producto>',views.edicionRest),
    path('IndexRest/eliminarRest/<Id_producto>',views.eliminarRest),
    path('IndexRest/editarRest/',views.editarRest,name='editarRest'),
    #Zonas Humedas Urls
     path('IndexZh/', views.homeZh,name="IndexZh"),
    path('IndexZh/registroZh/', views.registroZh,name='registroZh'),
    path('IndexZh/edicionZh/<Id_productoZH>',views.edicionZh),
    path('IndexZh/eliminarZh/<Id_productoZH>',views.eliminarZh),
    path('IndexZh/editarZh/',views.editarZh,name='editarZh'),

]
