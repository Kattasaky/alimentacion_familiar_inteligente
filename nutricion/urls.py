from django.urls import path
from .views import lista_platos, menu_semanal

urlpatterns = [
    path('platos/', lista_platos, name='platos'),
    path('', menu_semanal, name='menu'),
]