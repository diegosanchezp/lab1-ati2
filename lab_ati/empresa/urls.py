from audioop import reverse
from django.urls import path

from . import views

app_name = "empresa"

urlpatterns = [
    path("<slug:business_id>/employees/create", views.CreateEmployeeView.as_view(), name="create-employee"),
    path("<slug:business_id>/employees/edit/<slug:pk>", views.EditEmployeeView.as_view(), name="edit-employee"),
    path("<slug:business_id>/employees/", views.ListEmployeeView.as_view(), name="list-employee"),
    path("<slug:business_id>/employees/delete/<slug:pk>", views.DeleteEmployeeView.as_view(), name="delete-employee"),
    path("<slug:business_id>/employees/<slug:pk>", views.DetailEmployeeView.as_view(), name="detail-employee")

]
