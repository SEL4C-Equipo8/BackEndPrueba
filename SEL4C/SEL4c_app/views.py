# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from .models import Usuario, Actividades, Modulos, EvidenciaModulos, Evaluaciones, ResultadoEvaluaciones, Estadisticas, ProgresoActividades, ProgresoUsuarios, Administrador
# from .serializers import UsuarioSerializer, ActividadesSerializer, ModulosSerializer, EvidenciaModulosSerializer, EvaluacionesSerializer, ResultadoEvaluacionesSerializer, EstadisticasSerializer, ProgresoActividadesSerializer, ProgresoUsuariosSerializer, AdministradorSerializer


# # ===== USUARIO =====
# class PerfilUsuarioView(generics.RetrieveUpdateAPIView):
#     queryset = Usuario.objects.all()
#     serializer_class = UsuarioSerializer
#     lookup_field = 'id'  # Esto define el campo por el cual buscar al usuario (en este caso, 'id')

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = UsuarioSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"message": "Datos de perfil actualizados"})

# class IniciarSesionView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         contrasena = request.data.get('contrasena')

#         if email and contrasena:
#             usuario = Usuario.objects.filter(email=email).first()

#             if usuario and usuario.check_password(contrasena):
#                 # Las credenciales son correctas, el usuario está autenticado
#                 return Response({"message": "Inicio de sesión exitosa"})
#             else:
#                 # Credenciales incorrectas
#                 return Response({"message": "Credenciales incorrectas"}, status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             # Faltan datos de inicio de sesión
#             return Response({"message": "Falta email o contraseña"}, status=status.HTTP_400_BAD_REQUEST)

# class RegistroUsuarioView(APIView):
#     def post(self, request):
#         serializer = RegistroUsuarioSerializer(data=request.data)

#         if serializer.is_valid():
#             # Crear un nuevo usuario con los datos proporcionados
#             Usuario.objects.create(
#                 username=serializer.validated_data['username'],
#                 email=serializer.validated_data['email'],
#                 grado_ac=serializer.validated_data['gradoAcademico'],
#                 institucion=serializer.validated_data['institucion'],
#                 genero=serializer.validated_data['genero'],
#                 edad=serializer.validated_data['edad'],
#                 pais=serializer.validated_data['pais']
#             )

#             return Response({"message": "Usuario registrado con éxito"})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # ===== EVALUACIONES =====
# class CargarResultadoEvaluacion(APIView):
#     def post(self, request):
#         serializer = ResultadoEvaluacionSerializer(data=request.data)

#         if serializer.is_valid():
#             # Crear un nuevo resultado de evaluación con los datos proporcionados
#             resultado_evaluacion = serializer.save()
#             return Response({"message": "Resultado subido."})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# # ====== EVIDENCIAS MODULOS =====
# class CargarEvidenciaModulo(APIView):
#     def post(self, request):
#         serializer = EvidenciaModulosSerializer(data=request.data)

#         if serializer.is_valid():
#             # Crear una nueva evidencia de módulo con los datos proporcionados
#             EvidenciaModulos.objects.create(
#                 id_respuesta=serializer.validated_data['idRespuesta'],
#                 id_modulo=serializer.validated_data['idModulo'],
#                 texto_res=serializer.validated_data['texto_res'],
#                 archivo_res=serializer.validated_data['archivo_res']
#             )

#             return Response({"message": "Actividad subida exitosamente"})
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# # ====== ACTIVIDADES =====


from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Usuario, Actividades, Modulos, EvidenciaModulos, Evaluaciones, ResultadoEvaluaciones, Estadisticas, ProgresoActividades, ProgresoUsuarios, Administrador
from django.shortcuts import get_object_or_404
from .serializers import UsuarioSerializer, ActividadesSerializer, ModulosSerializer, EvidenciaModulosSerializer, EvaluacionesSerializer, ResultadoEvaluacionesSerializer, EstadisticasSerializer, ProgresoActividadesSerializer, ProgresoUsuariosSerializer, AdministradorSerializer


# Importa tus modelos y serializadores aquí

class UserProfileView(APIView):
    def get(self, request, user_id):
        usuario = get_object_or_404(Usuario, id_usuario=user_id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    def put(self, request, user_id):
        usuario = get_object_or_404(Usuario, id_usuario=user_id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Datos de perfil actualizados"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Implementa las vistas para los otros endpoints de manera similar

class UserLoginView(APIView):
    def get(self, request):
        # Implementa la lógica de inicio de sesión aquí
        return Response({"message": "Inicio de sesión exitosa"})

class UserSignupView(APIView):
    def post(self, request):
        # Implementa la lógica de registro de usuarios aquí
        return Response({"message": "Usuario registrado con éxito"})

class UploadEvaluationResultsView(APIView):
    def post(self, request):
        # Implementa la lógica para subir resultados de evaluaciones aquí
        return Response({"message": "Resultado subido"})

class UploadModuleEvidenceView(APIView):
    def post(self, request):
        # Implementa la lógica para subir evidencias de módulos aquí
        return Response({"message": "Evidencia subida exitosamente"})

# CRUD de actividades y módulos
class ActivityDetailView(APIView):
    def get(self, request, id_actividad):
        actividad = get_object_or_404(Actividades, id_actividad=id_actividad)
        serializer = ActividadesSerializer(actividad)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActividadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Actividad publicada con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id_actividad):
        actividad = get_object_or_404(Actividades, id_actividad=id_actividad)
        serializer = ActividadesSerializer(actividad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Actividad actualizada con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_actividad):
        actividad = get_object_or_404(Actividades, id_actividad=id_actividad)
        actividad.delete()
        return Response({"message": "Actividad eliminada con éxito"})





