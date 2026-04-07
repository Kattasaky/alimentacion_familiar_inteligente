from django.shortcuts import render
from .models import Plato

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'lista_platos.html', {'platos': platos})