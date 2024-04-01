from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index, name='index'),
    path('login/', views.login, name='Login'),
    path('indexadmin/', views.indexAdmin, name='indexAdmin'),
    path('indexusu/', views.indexUsu, name='indexUsu'),
    path('logout/', views.logout_view, name='Logout'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('servicios/', include('Aplicaciones.Servicios.urls')),
    path('habitaciones/', include('Aplicaciones.Habitaciones.urls')),
]
