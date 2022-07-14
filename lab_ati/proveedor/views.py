from django.shortcuts import render
from django.http import HttpResponse
from .models import Proveedor
from .forms import ProveedorForm
from ..empresa.models import Empresa


def createProveedor(request):
  if request.method == 'GET':
    empresaId = request.GET.get('empresa') 
    if(empresaId == None):
      return render(request,'404.html')
    empresa = Empresa.objects.get(id=empresaId)
    if(empresa == None):
      return render(request,'404.html')
    print(empresa)
    context = {}
    context["data"] = { "empresa":{"id":empresaId,"nombre":empresa.nombre},"update":True}
    return render(request,'proveedor/create-update.html')
  elif request.method == 'POST':
    formularioProveedor = ProveedorForm(request.POST or None)
    if formularioProveedor.is_valid():
      formularioProveedor.save()
      return HttpResponse('guardado!')
    return render(request,'proveedor/create-update.html')
    
    


#listar proeedores de una emrpresa dada
def listProveedor(request):
  empresaId = request.GET.get('empresa')
  print(empresaId)
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
  if request.method == 'GET':
    proveedorId = request.GET.get('proveedor')
    print('proveedor id: ', proveedorId)
    if(proveedorId == None):
      return render(request,'404.html')
    proveedor = Proveedor.objects.get(id=proveedorId)
    if(proveedor == None):
      return render(request,'404.html')
    print(proveedor)
    context = {
      "data":{
        "proveedor":proveedor,
        "update":True
      }
      
    }
    print(context)
    return render(request,'proveedor/create-update.html',context)
  elif request.method == 'POST':
    proveedorId = request.GET.get('proveedor')
    print('proveedor id: ', proveedorId)
    if(proveedorId == None):
      return render(request,'404.html')
    oldProveedor = Proveedor.objects.get(id=proveedorId)
    if(oldProveedor == None):
      return render(request,'404.html')

def deleteProveedor(request):
  proveedorId = request.GET.get('proveedor') 
  if(proveedorId == None):
    return render(request,'404.html')
  proveedor = Proveedor.objects.get(id=proveedorId)
  if(proveedor == None):
    return render(request,'404.html')
  proveedor.delete()
  return render(request,'proveedor/list.html')

def seeProveedor(request):
  proveedorId = request.GET.get('proveedor') 
  if(proveedorId == None):
    return render(request,'404.html')
  proveedor = Proveedor.objects.get(id=proveedorId)
  if(proveedor == None):
    return render(request,'404.html')
  context = {
    "proveedor" :proveedor,
  }
  return render(request,'proveedor/read.html', context)

##otras funciones
def findEmpresa(empresaId):
  empresa = Empresa.objects.get(id=empresaId)
  return empresa

