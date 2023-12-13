from django.urls import path
from . import views
from .views import pacientes, registroPaciente, EditarPaciente, EliminarPaciente

urlpatterns = [
    path('', views.home, name='home'),
    path('verpacientes/', pacientes.as_view() , name='pacientes'),
    path('formularioRegistro/', registroPaciente.as_view(), name='formularioRegistro'),
    path('editar_registro/<int:pk>/', EditarPaciente.as_view(), name='editar_registro'),
    path('eliminar_registro/<int:pk>/', EliminarPaciente.as_view(), name='eliminar_registro'),
]