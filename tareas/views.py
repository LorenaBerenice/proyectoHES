from django.shortcuts import render
from django.views import View
from .models import Registro
from .forms import RegistroForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def home(request):
    return render(request, 'home.html')

class pacientes(ListView):
    model = Registro
    template_name = 'listadoPacientes.html'
    context_object_name = 'registros'

class registroPaciente(CreateView):
    model = Registro
    template_name = 'registrarPaciente.html'
    form_class = RegistroForm
    context_object_name = 'registros'
    success_url = reverse_lazy('pacientes')

    def form_valid(self, form):
        return super().form_valid(form)

class EditarPaciente(UpdateView):
    model = Registro
    template_name = 'registrarPaciente.html'
    form_class = RegistroForm
    success_url = reverse_lazy('pacientes')

    def form_valid(self, form):
        return super().form_valid(form)

class EliminarPaciente(DeleteView):
    model = Registro
    template_name = 'eliminarPaciente.html'
    success_url = reverse_lazy('pacientes')