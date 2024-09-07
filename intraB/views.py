from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.db import connections
#from .models import AuthUser

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Llamada a la función de Django
            return redirect('principal')  # Redirige a la página principal

    return render(request, 'login.html')


@login_required
def principal(request):
    return render(request, 'principal.html')


@login_required
def mis_datos(request):
    return render(request, 'mis_datos.html')
