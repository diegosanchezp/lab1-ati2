from django import forms

COUNTRY_CHOICES = (
    ("0", "Selecciona..."),
    ("ve", "Venezuela"),
    ("ec", "Ecuardo"),
    ("es", "España"),
)


# creating a form
class CreateEmployeeForm(forms.Form):
    nombre = forms.CharField(
        label="Nombre",
        required=True,
        error_messages={
            "required": "El campo nombre es requerido",
        },
        widget=forms.TextInput(
            attrs={
                "id": "nombre",
                "name": "nombre",
                "class": "form-control",
                "placeholder": "Inserte un nombre",
            }
        ),
    )
    apellidos = forms.CharField(
        label="Apellidos",
        required=True,
        error_messages={
            "required": "El campo apellidos es requerido",
        },
        widget=forms.TextInput(
            attrs={
                "id": "apellidos",
                "name": "apellidos",
                "class": "form-control",
                "placeholder": "Inserte apellidos",
            }
        ),
    )
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
                "class": "form-control",
            },
        ),
        choices = COUNTRY_CHOICES
    )