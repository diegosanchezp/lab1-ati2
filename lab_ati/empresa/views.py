from audioop import reverse

from django.views.generic import UpdateView, CreateView, ListView, DeleteView, DetailView
from .forms import CreateEmployeeForm
from lab_ati.empresa.models import Empleado, Empresa
from django.urls import reverse

# Create your views here.

class CreateEmployeeView(CreateView):
    template_name = "pages/employees/create.html"
    model = Empleado
    form_class = CreateEmployeeForm

    def post(self, request, *args, **kwargs):
        self.success_url = self.request.build_absolute_uri()
        form = self.get_form()
        self.object = None

        if not Empresa.objects.get(id=self.request.POST['empresa']):
            return self.form_invalid(form)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_id'] = self.kwargs['business_id']
        return context


class EditEmployeeView(UpdateView):
    template_name = "pages/employees/create.html"
    model = Empleado
    form_class = CreateEmployeeForm
    pk_url_kwarg = 'pk'

    def post(self, request, *args, **kwargs):
        self.success_url = self.request.build_absolute_uri()
        form = self.get_form()
        self.object = self.get_object()

        self.request.POST._mutable = True
        self.request.POST['empresa'] = kwargs['business_id']
        self.request.POST._mutable = False

        if not Empresa.objects.get(id=kwargs['business_id']):
            return self.form_invalid(form)

        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):

        if businessId := self.kwargs.get('business_id'):
            if queryset is None:
                queryset = self.get_queryset()
            else:
                empresa = Empresa.objects.get(id=businessId)
                queryset.filter(empresa=empresa)

        return super().get_object(queryset) 

class ListEmployeeView(ListView):
    template_name = "pages/employees/list.html"
    model = Empleado
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context['business_id'] = self.kwargs['business_id']
        return context

    def get_queryset(self):
        queryset = Empleado.objects.filter(empresa = self.kwargs['business_id'])
        return queryset


class DeleteEmployeeView(DeleteView):
    template_name = "pages/employees/delete.html"
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context['business_id'] = self.kwargs['business_id']
        return context

    def get_success_url(self):
        return reverse('empresa:list-employee', kwargs={ 'business_id': self.kwargs['business_id']})
 
class DetailEmployeeView(DetailView): 
    template_name = "pages/employees/detail.html"
    model = Empleado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)     
        context['business_id'] = self.kwargs['business_id']
        return context

