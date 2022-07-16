from audioop import reverse
from django.http.response import Http404
from django.urls.base import reverse_lazy

from django.views.generic import UpdateView, CreateView, ListView, DeleteView, DetailView
from .forms import CreateEmployeeForm, SocialMediaFormset
from lab_ati.empresa.models import Empleado, Empresa, SocialMedia
from django.urls import reverse
from django.utils.translation import gettext as _
from django.core import exceptions
from lab_ati.utils.social_media import add_social_media

# Create your views here.

class CreateEmployeeView(CreateView):
    template_name = "pages/employees/create.html"
    model = Empleado
    form_class = CreateEmployeeForm
    success_url = "/"

    def get_empresa(self):

        # Validate that Empresa exists
        try:
            empresa = Empresa.objects.get(id=self.kwargs.get("business_id"))
        except (Empresa.DoesNotExist, exceptions.ValidationError):
            raise Http404(_("La empresa no existe"))

        return empresa

    def post(self, request, *args, **kwargs):
        self.object = None

        # Validate that Empresa exists
        self.empresa = self.get_context_data()["empresa"]

        self.social_media_formset = SocialMediaFormset(data=self.request.POST)

        # Call parent class post
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        # Override form valid method to add socialmedia
        # functionality

        if not self.social_media_formset.is_valid():
            return self.media_form_invalid(form)

        res = super().form_valid(form)
        # Add social media to Empleado
        add_social_media(self.object, self.social_media_formset)
        return res

    def media_form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                socialm_formset=self.social_media_formset
            )
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['business_id'] = self.kwargs['business_id']
        context["empresa"] = self.get_empresa()
        context["socialm_formset"] = SocialMediaFormset(queryset=SocialMedia.objects.none())
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

