from django.shortcuts import render, redirect
from django.http import HttpResponse
from lab_ati.cliente.models import Cliente
from lab_ati.cliente.forms import ClienteForm

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'pages/clientes/index.html', {'clientes':clientes})

def ver_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    form = ClienteForm(request.POST or None, instance=cliente)
    return render(request, 'pages/clientes/verCliente.html', {'form':form})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    return render(request, 'pages/clientes/crear.html', {'form':form})


def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect('clientes')

def editar_cliente(request, id):
    cliente = Cliente.objects.get(id = id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid() and request.POST:
        form.save()
        return redirect('clientes')
    return render(request, 'pages/clientes/editar.html', {'form':form})