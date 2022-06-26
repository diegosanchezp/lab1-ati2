from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class DirABC(models.Model):

    ciudad = models.TextField(_("Ciudad"))
    pais = models.TextField(_("Pais"))
    redes_sociales = GenericRelation(
        to="empresa.SocialMedia",
        related_query_name="redes_sociales"
    )

    class Meta:
        abstract = True

class EmpresaABC(DirABC):
    nombre = models.TextField(_("Nombre"))
    id_tributaria = models.TextField(_("Número de identificación tributaria"))
    email = models.EmailField(_("Email"))
    direccion = models.TextField(_("Dirección"))
    web_site = models.URLField(_("Sitio web"))
    servicio_proporciona = models.TextField(_("Servicio que proporciona"))

    def __str__(self):
        return f"{self.nombre} {self.id_tributaria}"

    class Meta:
        abstract = True

class Empresa(EmpresaABC):
    servicio_ofrecido = models.TextField(_(" Servicio que le ofrecimos"))
    servicio_proporciona = models.TextField(_("Servicio que proporciona"))
    whatsapp=models.TextField(_("Whatsapp"))
    telefono=models.TextField(_("Teléfono"))
    curso_interes=models.TextField(_("Curso de interés"))
    frecuencia=models.TextField(_("Frecuencia con la que desea mantenerse informado"))


# Generic Model
class SocialMedia(models.Model):
    nombre = models.TextField()
    valor = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
    def __str__(self):
        return f"{self.nombre} {self.valor}"

class Empleado(DirABC):

    class Modalidad(models.TextChoices):
        FIJO='FIJO', _('Fijo')
        HONORARIO_PROFESIONALES='HP', _('Honorario profesionales')

    nombre = models.TextField(_("Nombre"))
    apellido = models.TextField(_("Apellido"))
    ci = models.TextField(_("Cédula o nro pasaporte"))
    cargo=models.TextField(_("Cargo"))

    empresa=models.ForeignKey(
        to="empresa.Empresa",
        on_delete=models.CASCADE,
        related_name="empleados",
        verbose_name=_("Empleados"),
    )
    modalidad_contratacion=models.TextField(
        verbose_name=_("Modalidad de contratación"),
        choices=Modalidad.choices
    )
    email_emp = models.EmailField(_("Correo electrónico de la empresa"))
    email_p = models.EmailField(_("Correo personal"))
    tlf_celular=models.TextField(_("Teléfono celular"))
    tlf_local=models.TextField(_("Teléfono local"))

    def __str__(self):
        return f"{self.nombre} {self.ci} {self.email_p}"

