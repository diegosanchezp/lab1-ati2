# Generated by Django 4.0.5 on 2022-07-03 15:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('ciudad', models.TextField(verbose_name='Ciudad')),
                ('pais', models.TextField(verbose_name='Pais')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('id_tributaria', models.TextField(verbose_name='Número de identificación tributaria')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('direccion', models.TextField(verbose_name='Dirección')),
                ('web_site', models.URLField(verbose_name='Sitio web')),
                ('servicio_ofrecido', models.TextField(verbose_name=' Servicio que le ofrecimos')),
                ('servicio_proporciona', models.TextField(verbose_name='Servicio que proporciona')),
                ('whatsapp', models.TextField(verbose_name='Whatsapp')),
                ('telefono', models.TextField(verbose_name='Teléfono')),
                ('curso_interes', models.TextField(verbose_name='Curso de interés')),
                ('frecuencia', models.TextField(verbose_name='Frecuencia con la que desea mantenerse informado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('valor', models.TextField()),
                ('object_id', models.CharField(max_length=255)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.TextField(verbose_name='Ciudad')),
                ('pais', models.TextField(verbose_name='Pais')),
                ('nombre', models.TextField(verbose_name='Nombre')),
                ('apellido', models.TextField(verbose_name='Apellido')),
                ('ci', models.TextField(verbose_name='Cédula o nro pasaporte')),
                ('cargo', models.TextField(verbose_name='Cargo')),
                ('modalidad_contratacion', models.TextField(choices=[('FIJO', 'Fijo'), ('HP', 'Honorario profesionales')], verbose_name='Modalidad de contratación')),
                ('email_emp', models.EmailField(max_length=254, verbose_name='Correo electrónico de la empresa')),
                ('email_p', models.EmailField(max_length=254, verbose_name='Correo personal')),
                ('tlf_celular', models.TextField(verbose_name='Teléfono celular')),
                ('tlf_local', models.TextField(verbose_name='Teléfono local')),
                ('empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='empresa.empresa', verbose_name='Empresa')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddIndex(
            model_name='socialmedia',
            index=models.Index(fields=['content_type', 'object_id'], name='empresa_soc_content_92e85a_idx'),
        ),
    ]
