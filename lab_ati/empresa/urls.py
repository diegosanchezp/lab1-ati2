from django.urls import path

from lab_ati.empresa.views import (
    empresas_list_view
)

app_name = "business"

urlpatterns = [
    path("", view=empresas_list_view, name="list")
]
