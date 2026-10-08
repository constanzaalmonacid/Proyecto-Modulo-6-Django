from django.test import TestCase
from django.contrib.auth.models import User
from .models import Proyecto, Tarea

class ProyectoModelTest(TestCase):
    def setUp(self):
        self.usuario = User.objects.create_user(username='coni', password='12345segura')
        self.proyecto = Proyecto.objects.create(
            nombre='Proyecto de prueba',
            descripcion='Descripción',
            propietario=self.usuario
        )

    def test_nombre_proyecto(self):
        self.assertEqual(str(self.proyecto), 'Proyecto de prueba')


class TareaModelTest(TestCase):
    def setUp(self):
        usuario = User.objects.create_user(username='usuario2', password='12345segura')
        proyecto = Proyecto.objects.create(nombre='Proyecto', propietario=usuario)
        self.tarea = Tarea.objects.create(
            proyecto=proyecto,
            titulo='Tarea de prueba',
            estado='pendiente'
        )

    def test_titulo_tarea(self):
        self.assertEqual(str(self.tarea), 'Tarea de prueba')
