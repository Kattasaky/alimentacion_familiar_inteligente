from django.shortcuts import render
from .models import Plato, MenuSemanal
from .utils import calcular_nutrientes_plato
from .utils import calcular_nutrientes_plato, generar_alertas
def lista_platos(request):
    platos = Plato.objects.all()
    datos = []

    for plato in platos:
        nutrientes = calcular_nutrientes_plato(plato)
        alertas = generar_alertas(nutrientes)

        datos.append({
            "plato": plato,
            "nutrientes": nutrientes,
            "alertas": alertas
        })

    return render(request, 'nutricion/lista_platos.html', {'datos': datos})
def menu_semanal(request):
    menus = MenuSemanal.objects.all()
    return render(request, 'nutricion/menu.html', {'menus': menus})