from django.urls import path
from lab_ati.cliente.views import (
    clientes,
    ver_cliente,
    crear_cliente,
    eliminar_cliente,
    editar_cliente
    )

urlpatterns = [
    path('', clientes, name='clientes'),
    path('ver/<int:id>', ver_cliente, name='ver_cliente'),
    path('crear', crear_cliente, name='crear_cliente'),
    path('eliminar/<int:id>', eliminar_cliente, name='eliminar_cliente'),
    path('editar/<int:id>', editar_cliente, name='editar_cliente')
]