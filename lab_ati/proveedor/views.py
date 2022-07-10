from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor
from ..empresa.models import Empresa
# Create your views here.

def createProveedor(request):
  empresaId = request.GET.get('empresa')
  print('empresa id: ', empresaId)
  if(empresaId == None):
    return render(request,'404.html')
  empresa = Empresa.objects.get(id=empresaId)
  if(empresa == None):
    return render(request,'404.html')
  print(empresa)
  context = {}
  context["empresa"] = {"id":empresaId,"nombre":empresa.nombre}
  context["type"] = 'CREAR'
  return render(request,'proveedor/create-update.html')

#listar proeedores de una emrpresa dada
def listProveedor(request):
  empresaId = request.GET.get('empresa')
  if(empresaId == None):
    return render(request,'404.html')

  empresa = findEmpresa(empresaId)
  print(empresa)
  if(empresa == None): #empresa no existe
    return render(request,'404.html')

  proveedoresList = Proveedor.objects.filter(empresa__id__contains=empresaId)
  print(proveedoresList)
  context = {}

  context["tieneProveedores"] = True
  if(len(proveedoresList)==0):
    context["tieneProveedores"] = False

  context["list"] = proveedoresList
  context["empresa"] = {"empresa":empresa, "id":empresaId}
  return render(request,'proveedor/list.html',context)
  

def updateProveedor(request):
  typeAction = 'update'
  proveedorId = request.GET.get('proid')
  print('proveedor id: ', proveedorId)
  if(proveedorId == None):
    return render(request,'404.html')
  proveedor = Proveedor.objects.get(id=proveedorId)
  if(proveedor == None):
    return render(request,'404.html')
  print(proveedor)
  context = {
    "proveedor":proveedor,
    "type":typeAction
  }
  print(context)
  return render(request,'proveedor/create-update.html')

def deleteProveedor(request):
  return render(request,'proveedor/create-update.html')

def seeProveedor(request):
  proveedores = Proveedor.objects.all()

  print('test lista proveedores ',proveedores)
  context = {
    "proveedores" :proveedores,
  }
  return render(request,'proveedor/read.html', context)

##otras funciones
def findEmpresa(empresaId):
  empresa = Empresa.objects.get(id=empresaId)
  return empresa