from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Usuario, Actividades, Modulos, EvidenciaModulos, Evaluaciones, ResultadoEvaluaciones, Estadisticas, ProgresoActividades, ProgresoUsuarios, Administrador
from .serializers import UsuarioSerializer, ActividadesSerializer, ModulosSerializer, EvidenciaModulosSerializer, EvaluacionesSerializer, ResultadoEvaluacionesSerializer, EstadisticasSerializer, ProgresoActividadesSerializer, ProgresoUsuariosSerializer, AdministradorSerializer

# ===== USUARIO =====
class PerfilUsuarioView(generics.RetrieveUpdateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    lookup_field = 'id'  # Esto define el campo por el cual buscar al usuario (en este caso, 'id')

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UsuarioSerializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Datos de perfil actualizados"})

class IniciarSesionView(APIView):
    def post(self, request):
        email = request.data.get('email')
        contrasena = request.data.get('contrasena')

        if email and contrasena:
            usuario = Usuario.objects.filter(email=email).first()

            if usuario and usuario.check_password(contrasena):
                # Las credenciales son correctas, el usuario está autenticado
                return Response({"message": "Inicio de sesión exitosa"})
            else:
                # Credenciales incorrectas
                return Response({"message": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Faltan datos de inicio de sesión
            return Response({"message": "Falta email o contraseña"}, status=status.HTTP_400_BAD_REQUEST)

class RegistroUsuarioView(APIView):
    def post(self, request):
        serializer = RegistroUsuarioSerializer(data=request.data)

        if serializer.is_valid():
            # Crear un nuevo usuario con los datos proporcionados
            Usuario.objects.create(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                grado_ac=serializer.validated_data['gradoAcademico'],
                institucion=serializer.validated_data['institucion'],
                genero=serializer.validated_data['genero'],
                edad=serializer.validated_data['edad'],
                pais=serializer.validated_data['pais']
            )

            return Response({"message": "Usuario registrado con éxito"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ===== EVALUACIONES =====
class CargarResultadoEvaluacion(APIView):
    def post(self, request):
        serializer = ResultadoEvaluacionSerializer(data=request.data)

        if serializer.is_valid():
            # Crear un nuevo resultado de evaluación con los datos proporcionados
            resultado_evaluacion = serializer.save()
            return Response({"message": "Resultado subido."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# ====== EVIDENCIAS MODULOS =====
class CargarEvidenciaModulo(APIView):
    def post(self, request):
        serializer = EvidenciaModulosSerializer(data=request.data)

        if serializer.is_valid():
            # Crear una nueva evidencia de módulo con los datos proporcionados
            EvidenciaModulos.objects.create(
                id_respuesta=serializer.validated_data['idRespuesta'],
                id_modulo=serializer.validated_data['idModulo'],
                texto_res=serializer.validated_data['texto_res'],
                archivo_res=serializer.validated_data['archivo_res']
            )

            return Response({"message": "Actividad subida exitosamente"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# ====== ACTIVIDADES =====



# Create your views here.
