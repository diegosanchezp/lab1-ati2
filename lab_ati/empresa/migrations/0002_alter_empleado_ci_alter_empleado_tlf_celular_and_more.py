# Generated by Django 4.0.5 on 2022-07-18 01:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='ci',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='ci_invalido', message='El campo debe ser una cédula de identidad o número de pasaporte', regex='^(([A-Z]-)[0-9]{1,3}\\.?[0-9]{1,3}\\.?[0-9]{1,3})$|^([0-9A-Z]{10})$')], verbose_name='Cédula o nro pasaporte'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tlf_celular',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='tlf_celular_invalido', message='El campo debe ser un número de teléfono', regex='^\\+?([0-9]{1,3}|[1]\\-?[0-9]{3})?\\-?([0-9]{1,4})\\-?([0-9]{3}\\-?[0-9]{2}\\-?[0-9]{2})$')], verbose_name='Teléfono celular'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='tlf_local',
            field=models.TextField(validators=[django.core.validators.RegexValidator(code='tlf_local_invalido', message='El campo debe ser un número de teléfono', regex='^\\+?([0-9]{1,3}|[1]\\-?[0-9]{3})?\\-?([0-9]{1,4})\\-?([0-9]{3}\\-?[0-9]{2}\\-?[0-9]{2})$')], verbose_name='Teléfono local'),
        ),
    ]
