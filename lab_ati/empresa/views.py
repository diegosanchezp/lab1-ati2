from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import UpdateView, CreateView
from .forms import CreateEmployeeForm
from lab_ati.empresa.models import Empleado

# Create your views here.

class CreateEmployeeView(CreateView):
    template_name = "pages/employees/create.html"
    model = Empleado
    form_class = CreateEmployeeForm

class EditEmployeeView(UpdateView):
    template_name = "pages/employees/create.html"
    model = Empleado
