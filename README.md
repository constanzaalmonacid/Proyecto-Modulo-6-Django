# Proyecto Módulo 6 - Django Web App

Aplicación web desarrollada con Django para gestionar proyectos y tareas.

## Funcionalidades

- Registro de usuarios
- Inicio y cierre de sesión
- Restricción de acceso mediante LoginRequiredMixin
- Crear, editar, listar y eliminar proyectos
- Crear, editar, listar y eliminar tareas
- Relación entre usuarios, proyectos y tareas
- Protección CSRF
- Sitio administrativo de Django
- Pruebas unitarias básicas

## Instalación

1. Crear un entorno virtual:

```bash
python -m venv venv
```

2. Activarlo en Windows:

```bash
venv\Scripts\activate
```

3. Instalar Django:

```bash
pip install -r requirements.txt
```

4. Crear migraciones:

```bash
python manage.py makemigrations
```

5. Aplicar migraciones:

```bash
python manage.py migrate
```

6. Crear superusuario:

```bash
python manage.py createsuperuser
```

7. Ejecutar servidor:

```bash
python manage.py runserver
```

8. Abrir en el navegador:

http://127.0.0.1:8000/

## Pruebas

```bash
python manage.py test
```
