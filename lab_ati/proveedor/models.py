from django.db import models
from lab_ati.empresa.models import EmpresaABC
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Proveedor(EmpresaABC):
    tlf=models.TextField(_("Teléfono del proveedor"))
    representante=models.TextField(_("Nombre del representante"))
    cargo=models.TextField(_("Cargo del representante"))
    email_representante=models.EmailField(_("Correo del representante"))
    email_personal_representante=models.EmailField(_("Correo personal del representante"))
    tlf_representate=models.TextField(_("Teléfono celular del representante"))
    tlf_local=models.TextField(_("Teléfono local del representante"))
    pais_representante=models.TextField(_("Pais de residencia de representante"))
    redes_representante=GenericRelation(
        to="empresa.SocialMedia",
        verbose_name=_("Redes sociales del representante"),
    )
    redes_proveedor=GenericRelation(
        to="empresa.SocialMedia",
        verbose_name=_("Redes sociales del proveedor"),
    )
    empresa=models.ForeignKey(
        to="empresa.Empresa",
        on_delete=models.CASCADE,
        related_name="proveedores",
        null=True,
        blank=True,
        verbose_name=_("Empresa"),
    )
