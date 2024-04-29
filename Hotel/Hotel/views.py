from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import logout_required
from django.contrib.auth.models import User

#Pagina Inicial
def index(request):
    message = "Bienvenido al Hotel Ares"
    return render(request, "Index.html", {'message': message})
#Redirrección Cliente
def indexUsu(request):
    if not request.user.is_authenticated:
        return redirect('login')  
    if request.user.is_staff:
        return redirect('index')  
    
    username = request.user.username
    message = f"Bienvenido al Hotel Ares, {username}"
    return render(request, "IndexUsu.html", {'message': message})
#Redirrección Usuarios y Login 
def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session['username'] = user.username  
            if user.is_staff:  
                return redirect('indexAdmin')
            else:
                return redirect('indexUsu')
        else:
            return render(request, 'login.html', {'error_message': 'Nombre de usuario o contraseña incorrectos.'})
    else:
        return render(request, 'login.html')

#Redirrección Admin

@login_required
def indexAdmin(request):
   if not request.user.is_staff:
        return redirect('index')  
   username = request.user.username
   message = f"Bienvenido Administrador, {username}"
   return render(request, "IndexAdmin.html", {'message': message})

#Logoutç
@logout_required
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión con éxito.")
    return redirect('index')

#Registro 
def register(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        user = User.objects.create_user(username=usuario, email=correo, password=contraseña)
        user.first_name = nombre
        user.last_name = apellido

        user.save()

        user = authenticate(username=usuario, password=contraseña)
        if user is not None:
            auth_login(request, user)
            
            return redirect('index')
        else:
            
            pass

    return render(request, 'register.html')