from django.shortcuts import render
from .models import Plato, MenuSemanal

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'nutricion/lista_platos.html', {'platos': platos})

def menu_semanal(request):
    menus = MenuSemanal.objects.all()
    return render(request, 'nutricion/menu.html', {'menus': menus})