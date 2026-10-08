from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('registro/', views.registro, name='registro'),

    path('login/', auth_views.LoginView.as_view(template_name='core/registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('proyectos/', views.ProyectoListView.as_view(), name='proyecto_list'),
    path('proyectos/nuevo/', views.ProyectoCreateView.as_view(), name='proyecto_create'),
    path('proyectos/<int:pk>/editar/', views.ProyectoUpdateView.as_view(), name='proyecto_update'),
    path('proyectos/<int:pk>/eliminar/', views.ProyectoDeleteView.as_view(), name='proyecto_delete'),

    path('tareas/', views.TareaListView.as_view(), name='tarea_list'),
    path('tareas/nueva/', views.TareaCreateView.as_view(), name='tarea_create'),
    path('tareas/<int:pk>/editar/', views.TareaUpdateView.as_view(), name='tarea_update'),
    path('tareas/<int:pk>/eliminar/', views.TareaDeleteView.as_view(), name='tarea_delete'),
]
