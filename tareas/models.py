from django.db import models

class Registro(models.Model):
    fecha_actual = models.DateField()
    periodo = models.CharField(max_length=20)
    id_alumno = models.CharField(max_length=20)
    nombre = models.CharField(max_length=100)
    id_sexo = models.CharField(max_length=1, choices=[('1', 'Hombre'), ('2', 'Mujer')])
    edad = models.CharField(max_length=3)
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=1, choices=[('1', 'Soltero(a)'), ('2', 'Casado(a)'), ('3', 'Unión libre'), ('4', 'Viudo(a)'), ('5', 'Divorciado(a)')])
    telefono_celular = models.CharField(max_length=15)
    carrera = models.CharField(max_length=50)
    semestre = models.CharField(max_length=20)
    ocupacion = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    condicion_salud = models.CharField(max_length=200)
    fecha_inicio_condicion = models.DateField()
    tratamiento = models.CharField(max_length=1, choices=[('1', 'Sí'), ('2', 'No')])
    atentado = models.CharField(max_length=1, choices=[('1', 'Ideación suicida'), ('2', 'Planeación suicida'), ('3', 'Intento suicida'), ('4', 'Ninguno')])
    fecha_atentado = models.DateField()
    descripcion_atentado = models.CharField(max_length=200)
    numero_emergencia = models.CharField(max_length=15)
    contacto_emergencia = models.CharField(max_length=100)
    parentesco_contacto_e = models.CharField(max_length=1, choices=[('1', 'Padre'), ('2', 'Madre'), ('3', 'Hermano'), ('4', 'Hermana'), ('5', 'Pareja'), ('6', 'Amistad')])
    conocimiento_servicio = models.CharField(max_length=1, choices=[('1', 'Por un amigo (a)'), ('2', 'Por publicación del grupo de teams'), ('3', 'Por indicación de un docente'), ('4', 'Por indicación de mi tutor (a)'), ('5', 'Por el servicio de enfermería'), ('6', 'Por la propaganda pegada en las paredes de la institución'), ('7', 'Otro')])
    motivo_consulta = models.CharField(max_length=1, choices=[('1', 'Académico'), ('2', 'Personal'), ('3', 'Familiar'), ('4', 'Social')])
    descripcion_consulta = models.CharField(max_length=200)
    expectativas_usuario = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
