from django.urls import path

from . import views

app_name = "empresa"

urlpatterns = [
    path("employees/create", views.CreateEmployeeView.as_view(), name="create-employee"),
    path("employees/edit/<slug:pk>", views.EditEmployeeView.as_view(), name="edit-employee")
]
