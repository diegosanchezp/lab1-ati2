# Generated by Django 4.0.5 on 2022-07-17 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.TextField(verbose_name='Ciudad')),
                ('pais', models.TextField(verbose_name='Pais')),
                ('nombre', models.TextField(verbose_name='Nombre y Apellido')),
                ('tipo', models.TextField(choices=[('LE', 'Labora empresa'), ('SO', 'Estudiante'), ('JR', 'Otro')])),
                ('empcompany', models.TextField(verbose_name='Compañia/Organismo')),
                ('cargo', models.TextField(verbose_name='Cargo')),
                ('personal_email', models.TextField(verbose_name='Email personal')),
                ('tlf_celular', models.TextField(verbose_name='Teléfono celular')),
                ('whatsapp', models.TextField(verbose_name='Whatsapp')),
                ('servicio_ofrecido', models.TextField(verbose_name='Servicio ofrecido')),
                ('curso_interes', models.TextField(verbose_name='Curso de interés')),
                ('frecuencia', models.TextField(verbose_name='Frecuencia con la que desea mantenerse informado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
