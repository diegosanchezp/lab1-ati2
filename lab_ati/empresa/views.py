from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core import serializers

from .models import Empresa


# Create your views here.
class EmpresasListView(LoginRequiredMixin, TemplateView):

    model = Empresa
    template_name = "empresa/empresa_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = serializers.serialize("json", Empresa.objects.all())
        return context

empresas_list_view = EmpresasListView.as_view()