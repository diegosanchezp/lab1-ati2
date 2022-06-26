from django.db import models
from lab_ati.empresa.models import EmpresaABC
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Proveedor(EmpresaABC):
    representante=models.TextField()
    cargo=models.TextField(_(""))
    email_representante=models.EmailField()
    tlf=models.TextField(_("Teléfono del proveedor"))
    tlf_representate=models.TextField(_("Teléfono celular del representante"))
    tlf_local=models.TextField(_("Teléfono local"))
    redes_representante=GenericRelation("empresa.SocialMedia")
    empresa=models.ForeignKey(
        to="empresa.Empresa",
        on_delete=models.CASCADE,
        related_name="proveedores",
        verbose_name=_("Proveedores"),
    )
