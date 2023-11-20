from django.http import HttpResponse
from django.db import IntegrityError
from infoTransporte.models import Cliente
from django.http import HttpResponseRedirect
from .forms import LogInUsuarios, RegCliente
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .model_func import prediction

cliente, creado = Group.objects.get_or_create(name='cliente')

def welcome( request ):
    return render(request, 'base.html')



def logIn(request):
    if request.method == 'POST':
        form = LogInUsuarios(request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect('welcome')
            
        else:
            error = "Los datos en algunos campos del formulario son incorrectos. Por favor, revíselos."
            return render(request, 'login.html', {'formulario': form, 'errorMsg': error})
    else:
        form = LogInUsuarios()
        if request.GET.get('error403') is None:
            error = None
        else:
            error = 'Operación no permitida. Use una cuenta con permisos suficientes'
        return render(request, 'login.html', {'formulario': form, 'errorMsg': error})


@login_required(login_url=reverse_lazy('login'))
def logOut( request ):
    logout( request )
    return redirect ('welcome')


def route(request):
    return render(request, 'route.html')

def map(request):
    return render(request,'map.html')

def bicimad_map(request):
    api_url = "https://rbdata.emtmadrid.es:8443/BiciMad/v1/getBiciMAD.svc/GetBikes"
    api_key = "YOUR_API_KEY"

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    try:
        response = request.get(api_url, headers=headers)
        data = response.json()
    except request.exceptions.RequestException as e:
        data = {'error': str(e)}

    return render(request, 'bicimad_map.html', {'bicimad_data': data})


def bicimad(request):
    return render(request, 'bicimad.html')

def regCliente(request):
    if request.method == 'POST':
        formulario = RegCliente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data['nombre']
            apellidos = formulario.cleaned_data['apellidos']
            dni = formulario.cleaned_data['dni']
            nombreUser = formulario.cleaned_data['nombreUser']
            contrasenya = formulario.cleaned_data['password']
            pacienteNuevo = Cliente(nombre=nombre, apellidos=apellidos, dni=dni, nombreUser=nombreUser)
            
            # Verificar si el grupo 'cliente' existe antes de intentar obtenerlo
            try:
                cliente = Group.objects.get(name='cliente')
            except Group.DoesNotExist:
                print("El grupo 'cliente' no existe en la base de datos.")
                # Puedes decidir manejar la situación de falta de grupo aquí
                return render(request, 'nuevo_cliente.html', {'formulario': formulario, 'errorMsg': 'El grupo "cliente" no existe en la base de datos.'})

            try:
                pacienteNuevo.save()
                user = User.objects.create_user(nombreUser, contrasenya)
                cliente.user_set.add(user)
                user.save()
                return redirect('welcome')
            except IntegrityError:
                error = "There is already a user with name: " + nombreUser
                return render(request, 'nuevo_cliente.html', {'formulario': formulario, 'errorMsg': error})
        else:
            error = "The data in some fields of the form are incorrect. Please check them."
            return render(request, 'nuevo_cliente.html', {'formulario': formulario, 'errorMsg': error})
    else:
        form = RegCliente()
    return render(request, 'nuevo_cliente.html', {'formulario': form})
