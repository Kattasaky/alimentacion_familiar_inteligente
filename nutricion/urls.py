from django.urls import path
from .views import lista_platos

urlpatterns = [
    path('', lista_platos),
]