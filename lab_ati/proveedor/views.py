from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Proveedor
from .forms import ProveedorForm
from ..empresa.models import Empresa
from django.template.defaulttags import register

@register.filter
def get_item(objectList, key):
  if objectList == "":
    return ""
  return getattr(objectList,key)

def createProveedor(request):
  if request.method == 'GET': 
    empresaId = request.GET.get('empresa') 
    if(empresaId == None):
      return render(request,'404.html')
    empresa = Empresa.objects.get(id=empresaId)
    if(empresa == None):
      return render(request,'404.html')
    print(empresa)
    formularioProveedor = ProveedorForm(request.POST or request.GET)
    context = {}
    context["data"] = { "empresa":empresa,"update":False, "formulario":formularioProveedor}
    return render(request,'pages/proveedor/create-update.html', context)

  elif request.method == 'POST':
    empresaId = request.GET.get('empresa') 
    if(empresaId == None):
      return render(request,'404.html')  
    empresa = Empresa.objects.get(id=empresaId)
    if(empresa == None):
      return render(request,'404.html')
    formularioProveedor = ProveedorForm(request.POST or None)
    print(formularioProveedor)
    if formularioProveedor.is_valid():
      print('is valid!')
      formularioProveedor.save()
    return redirect('/proveedor?empresa='+empresaId)
    
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
    formularioProveedor = ProveedorForm(request.POST or request.GET)
    context = {
      "data":{
        "proveedor":proveedor,
        "empresa":{"id":proveedor.empresa.id},
        "update":True,
        "formulario":formularioProveedor
      }
    }
    return render(request,'pages/proveedor/create-update.html',context)
  elif request.method == 'POST':
    proveedorId = request.GET.get('proveedor')
    print('proveedor id: ', proveedorId)
    if(proveedorId == None):
      return render(request,'404.html')
    oldProveedor = Proveedor.objects.get(id=proveedorId)
    if(oldProveedor == None):
      return render(request,'404.html')
    print(oldProveedor)
    formularioProveedor = ProveedorForm(request.POST, instance=oldProveedor)
    print(formularioProveedor)
    empresaId = str(oldProveedor.empresa.id)
    if formularioProveedor.is_valid():
      print('is valid!')
      formularioProveedor.save()
    return redirect('/proveedor?empresa='+empresaId)


#listar proeedores de una emrpresa dada
def listProveedor(request):
  empresaId = request.GET.get('empresa')
  print(empresaId)
  if(empresaId == None):
    return render(request,'pages/404.html')

  empresa = findEmpresa(empresaId)
  print(empresa)
  if(empresa == None): #empresa no existe
    return render(request,'pages/404.html')

  proveedoresList = Proveedor.objects.filter(empresa__id__contains=empresaId)
  print(proveedoresList)
  context = {}

  context["tieneProveedores"] = True
  if(len(proveedoresList)==0):
    context["tieneProveedores"] = False

  context["list"] = proveedoresList
  context["empresa"] = {"empresa":empresa, "id":empresaId}
  return render(request,'pages/proveedor/list.html',context)
  



def deleteProveedor(request):
  proveedorId = request.GET.get('proveedor') 
  if(proveedorId == None):
    return render(request,'pages/404.html')
  proveedor = Proveedor.objects.get(id=proveedorId)
  if(proveedor == None):
    return render(request,'pages/404.html')
  proveedor.delete()
  empresaId = str(proveedor.empresa.id)
  return redirect('/proveedor?empresa='+empresaId)

def seeProveedor(request):
  proveedorId = request.GET.get('proveedor') 
  if(proveedorId == None):
    return render(request,'pages/404.html')
  proveedor = Proveedor.objects.get(id=proveedorId)
  if(proveedor == None):
    return render(request,'pages/404.html')
  context = {
    "proveedor" :proveedor,
  }
  return render(request,'pages/proveedor/read.html', context)

##otras funciones
def findEmpresa(empresaId):
  empresa = Empresa.objects.get(id=empresaId)
  return empresa

