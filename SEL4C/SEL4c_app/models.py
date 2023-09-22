from django.db import models

"""
from django.contrib.auth.models import AbstractUser

usuario = Usuario.objects.create(username='nombre_de_usuario', email='correo@example.com')
usuario.set_password('contrasena_en_texto_plano')  # Esto almacenará la contraseña como hash
usuario.save()

class Usuario(AbstractUser):
    # Campos adicionales personalizados
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    grado_ac = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    genero = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    pais = models.CharField(max_length=100, choices=PAISES)

    def __str__(self):
        return self.username
"""

# Opciones para el campo 'pais'
PAISES = (
    ('opcion1', 'Opción 1'),
    ('opcion2', 'Opción 2'),
)

# ==== TABLA USUARIOS ====
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    grado_ac = models.CharField(max_length=100)
    institucion = models.CharField(max_length=200)
    genero = models.CharField(max_length=20)
    edad = models.IntegerField()
    pais = models.CharField(max_length=100, choices=PAISES)

    def __str__(self):
        return self.username

"""
from django.core.validators import FileExtensionValidator

class Usuario(models.Model):
    photo = models.ImageField(upload_to='photos/', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
"""


# ==== TABLA ACTIVIDADES ====
class Actividades(models.Model):
    id_actividad = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    imagen = models.FileField(upload_to='actividad_imagenes/', null=True, blank=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo


# ==== TABLA MODULOS ====
class Modulos(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    id_actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)
    titulo_mod = models.CharField(max_length=100)
    instrucciones = models.CharField(max_length=255)
    imagen_mod = models.FileField(upload_to='modulo_imagenes/', null=True, blank=True)
    tipo_multimedia = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo_mod


# ==== TABLA EVIDENCIAS MODULOS ====
class EvidenciaModulos(models.Model):
    id_respuesta = models.AutoField(primary_key=True)
    id_modulo = models.OneToOneField(Modulos, on_delete=models.CASCADE)
    texto_res = models.CharField(max_length=255)
    archivo_res = models.FileField(upload_to='evidencia_archivos/', null=True, blank=True)

    def __str__(self):
        return f"Evidencia de {self.modulo.titulo_mod}"


# ==== TABLA EVALUACIONES ====
class Evaluaciones(models.Model):
    id_evaluacion = models.AutoField(primary_key=True)
    tipo_evaluacion = models.CharField(max_length=100)
    imagen_env = models.FileField(upload_to='evaluacion_imagenes/', null=True, blank=True)

    def __str__(self):
        return f"Evaluación tipo {self.tipo_evaluacion}"


# ==== TABLA RESULTADO EVALUACIONES ====
class ResultadoEvaluaciones(models.Model):
    id_resultado = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_evaluacion = models.OneToOneField(Evaluaciones, on_delete=models.CASCADE)
    competencia_1 = models.IntegerField()
    competencia_2 = models.IntegerField()
    competencia_3 = models.IntegerField()
    competencia_4 = models.IntegerField()
    competencia_5 = models.IntegerField()   

    def __str__(self):
        return f"Resultados de la evaluación de {self.evaluacion.usuario.username}"


# ==== TABLA ESTADISTICAS ====
class Estadisticas(models.Model):
    id_estadistica = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    actividades = models.IntegerField()
    evidencias = models.IntegerField()
    progreso = models.IntegerField()

    def __str__(self):
        return f"Estadísticas de {self.usuario.username}"


# ==== TABLA PROGRESO ACTIVIDADES ====
class ProgresoActividades(models.Model):
    id_progreso = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    actividad1 = models.BooleanField(default=False)
    actividad2 = models.BooleanField(default=False)
    actividad3 = models.BooleanField(default=False)
    actividad4 = models.BooleanField(default=False)

    def __str__(self):
        return f"Progreso de actividades de {self.usuario.username}"


# ==== TABLA PROGRESO USUARIOS ====
class ProgresoUsuarios(models.Model):
    id_progreso_usuario = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_actividad = models.ForeignKey(Actividades, on_delete=models.CASCADE)
    id_modulo = models.ForeignKey(Modulos, on_delete=models.CASCADE)
    estado_actividad = models.BooleanField(default=False)
    estado_modulo = models.BooleanField(default=False)

    def __str__(self):
        return f'Progreso de Usuario {self.id_usuario} en Actividad {self.id_actividad}'


# ==== TABLA ADMINISTRADOR ====
class Administrador(models.Model):
    id_admin = models.AutoField(primary_key=True)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    resultados_evaluaciones = models.ManyToManyField(ResultadoEvaluaciones)
    evidencias_modulos = models.ManyToManyField(EvidenciaModulos)
    progreso_actividades = models.ManyToManyField(ProgresoActividades)
    estadisticas = models.ManyToManyField(Estadisticas)

    def __str__(self):
        return self.username