# Generated by Django 4.0.5 on 2022-07-12 23:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('ciudad', models.TextField(verbose_name='Ciudad')),
                ('pais', models.TextField(verbose_name='Pais')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('id_tributaria', models.TextField(verbose_name='Número de identificación tributaria')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('web_site', models.URLField(verbose_name='Sitio web')),
                ('servicio_proporciona', models.TextField(verbose_name='Servicio que proporciona')),
                ('representante', models.TextField(verbose_name='Representante')),
                ('cargo', models.TextField(verbose_name='Cargo')),
                ('email_representante', models.EmailField(max_length=254, verbose_name='Correo del representante de  la empresa')),
                ('email_personal_representante', models.EmailField(max_length=254, verbose_name='Correo personal del representante')),
                ('tlf', models.TextField(verbose_name='Teléfono del proveedor')),
                ('tlf_representate', models.TextField(verbose_name='Teléfono celular del representante')),
                ('tlf_local', models.TextField(verbose_name='Teléfono local')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proveedores', to='empresa.empresa', verbose_name='Empresa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
