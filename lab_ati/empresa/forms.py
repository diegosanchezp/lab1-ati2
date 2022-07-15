from django import forms

from lab_ati.empresa.models import Empleado

COUNTRY_CHOICES = (
    ("", "Selecciona..."),
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

    class Meta:
        model = Empleado
        fields = "__all__"

