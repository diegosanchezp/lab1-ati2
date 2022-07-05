from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .forms import CreateEmployeeForm

# Create your views here.

def CreateEmployeeView(request: HttpRequest) -> HttpResponse:
    form = CreateEmployeeForm()
    context = {}
    context["form"] = form
    return render(request, "pages/employees/create.html", context)
