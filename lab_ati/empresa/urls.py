from django.urls import path

from . import views

app_name = "empresa"

urlpatterns = [
    path("employees/create", views.CreateEmployeeView, name="create-employee")
]
