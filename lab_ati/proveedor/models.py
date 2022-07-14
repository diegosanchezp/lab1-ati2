from django.db import models
from lab_ati.empresa.models import EmpresaABC
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Proveedor(EmpresaABC):
    representante=models.TextField(_("Representante"))
    cargo=models.TextField(_("Cargo"))
    email_representante=models.EmailField(_("Correo del representante de  la empresa"))
    email_personal_representante=models.EmailField(_("Correo personal del representante"))
    tlf=models.TextField(_("Teléfono del proveedor"))
    tlf_representate=models.TextField(_("Teléfono celular del representante"))
    tlf_local=models.TextField(_("Teléfono local"))
    pais_representante=models.TextField(_("Pais de residencia"))
    redes_representante=GenericRelation(
        to="empresa.SocialMedia",
        verbose_name=_("Redes sociales del representante"),
    )
    empresa=models.ForeignKey(
        to="empresa.Empresa",
        on_delete=models.CASCADE,
        related_name="proveedores",
        null=True,
        blank=True,
        verbose_name=_("Empresa"),
    )
