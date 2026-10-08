from django.contrib import admin
from .models import Proyecto, Tarea

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'propietario', 'fecha_creacion')
    search_fields = ('nombre', 'propietario__username')


@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'proyecto', 'estado', 'fecha_limite')
    list_filter = ('estado',)
    search_fields = ('titulo', 'proyecto__nombre')
