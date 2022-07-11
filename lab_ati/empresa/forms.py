from django import forms

from lab_ati.empresa.models import Empleado

COUNTRY_CHOICES = (
    ("0", "Selecciona..."),
    ("ve", "Venezuela"),
    ("ec", "Ecuador"),
    ("es", "España"),
)


# creating a form
class CreateEmployeeForm(forms.ModelForm):
    """
    Formulario del modelo empleado
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        # Set custom widget attr
        for field in  self.fields.values():
            if isinstance(field, forms.fields.CharField):
                if isinstance(field.widget, forms.widgets.Textarea):
                    field.widget = forms.TextInput(attrs={
                        "required": True,
                    })

                field.widget.attrs.update({
                    "class": "form-control",
                })

            if isinstance(field.widget, forms.widgets.Select):
                field.widget.attrs.update({
                    "class": "form-select",
                })

    # Override pais field
    pais = forms.ChoiceField(
        label="Pais",
        required=True,
        error_messages={
            "required": "El campo pais es requerido",
        },
        widget=forms.Select(
            attrs = {
                "id": "pais",
                "name": "pais",
                "class": "form-select",
            },
        ),
        choices = COUNTRY_CHOICES
    )

    class Meta:
        model = Empleado
        fields = "__all__"

