from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import RegistroForm, ProyectoForm, TareaForm
from .models import Proyecto, Tarea


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('dashboard')
    else:
        form = RegistroForm()
    return render(request, 'core/register.html', {'form': form})


@login_required
def dashboard(request):
    proyectos = Proyecto.objects.filter(propietario=request.user)
    tareas = Tarea.objects.filter(proyecto__propietario=request.user)
    return render(request, 'core/dashboard.html', {
        'proyectos': proyectos,
        'tareas': tareas,
    })


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    template_name = 'core/proyecto_list.html'
    context_object_name = 'proyectos'

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class ProyectoCreateView(LoginRequiredMixin, CreateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        return super().form_valid(form)


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
    model = Proyecto
    form_class = ProyectoForm
    template_name = 'core/proyecto_form.html'
    success_url = reverse_lazy('proyecto_list')

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = 'core/proyecto_confirm_delete.html'
    success_url = reverse_lazy('proyecto_list')

    def get_queryset(self):
        return Proyecto.objects.filter(propietario=self.request.user)


class TareaListView(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'core/tarea_list.html'
    context_object_name = 'tareas'

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__propietario=self.request.user)


class TareaCreateView(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'core/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


class TareaUpdateView(LoginRequiredMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'core/tarea_form.html'
    success_url = reverse_lazy('tarea_list')

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__propietario=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['usuario'] = self.request.user
        return kwargs


class TareaDeleteView(LoginRequiredMixin, DeleteView):
    model = Tarea
    template_name = 'core/tarea_confirm_delete.html'
    success_url = reverse_lazy('tarea_list')

    def get_queryset(self):
        return Tarea.objects.filter(proyecto__propietario=self.request.user)
