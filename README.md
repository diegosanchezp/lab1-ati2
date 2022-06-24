# Lab 1 ATI-2

## Setup ambiente de desarrollo
Estas son las dependencias que tienen que tener instaladas en su sistema operativo para levantar el ambiente de desarrollo
1. docker
2. docker-compose

En la carpeta del repositorio, correr los siguientes comandos

Descargar las imágenes de docker

```bash
docker-compose -f local.yml pull
```

Si estas utilizando linux poner esto en tu `.bashrc` o `.zhsrc`, se necesita para los permisos de archivos

```bash
export UID=$(id -u)
export GID=$(id -g)
```

Activar servicio de base de datos
```bash
docker-compose -f local.yml up -d postgres
```

Crear entorno virtual de python y descargar dependencias, al final te pedirá credenciales, estas son para el usuario administrador

Pon las siguiente

- Username: admin
- Email: dev@dev
- Password: dev123456

```bash
docker-compose -f local.yml run -w /app --entrypoint bash --rm django setup_dev.sh
```

Iniciar servicios de docker

```bash
docker-compose -f local.yml up -d
```
Visitar `127.0.0.1:8000`

El ultimo comando es el comando que tienes que ejecutar para levantar el ambiente de desarrollo.

## Comandos basicos para el desarrollo

Ver los logs de django
```bash
docker-compose -f local.yml logs -f django
```

Iniciar una terminal interactiva en el contenedor de docker
```bash
docker-compose -f local.yml run -w /app --entrypoint bash django
```

Y después activar el entorno virtual de python
```bash
source .venv/bin/activate
```

Lo anterior sirve para correr cualquier comando que utilice las dependencias del entorno virtual como por ejemplo

```bash
python manage.py makemigrations
```
### Creación de usuarios

Cuando creas un usuario en http://127.0.0.1:8000/accounts/signup/, mandara un email de confirmación de cuenta, el email lo encontraras en los logs de django

```bash
docker-compose -f local.yml logs -f django
```
## Documentacion adicional
Este repositorio esta basado en [django-cookie-cutter](https://cookiecutter-django.readthedocs.io/en/latest/)

