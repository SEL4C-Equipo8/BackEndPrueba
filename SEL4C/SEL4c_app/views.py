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

class ModuleDetailView(APIView):
    def get(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        serializer = ModulosSerializer(modulo)
        return Response(serializer.data)

    def post(self, request, id_actividad):
        data = request.data
        data['id_actividad'] = id_actividad  # Asigna el ID de la actividad desde la URL a los datos
        serializer = ModulosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Módulo agregado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        serializer = ModulosSerializer(modulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Módulo actualizado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        modulo.delete()
        return Response({"message": "Módulo eliminado con éxito"})

class AdminListView(APIView):
    def get(self, request):
        administradores = Administrador.objects.all()
        serializer = AdministradorSerializer(administradores, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AdministradorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Administrador creado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminDetailView(APIView):
    def get(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        serializer = AdministradorSerializer(admin)
        return Response(serializer.data)

    def put(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        serializer = AdministradorSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Administrador actualizado exitosamente"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        admin.delete()
        return Response({"mensaje": "Administrador eliminado exitosamente"})

class AdminDashboardView(APIView):
    def get(self, request):
        return Response({"mensaje": "Panel de control del administrador"})

class AdminPersonalProgressView(APIView):
    def get(self, request, user_id):
        try:
            usuario = Usuario.objects.get(id_usuario=user_id)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_inicial = ResultadoEvaluaciones.objects.filter(usuario=usuario, tipo_evaluacion="inicial").first()
        resultado_evaluacion_final = ResultadoEvaluaciones.objects.filter(usuario=usuario, tipo_evaluacion="final").first()

        if not resultado_evaluacion_inicial or not resultado_evaluacion_final:
            return Response({"error": "Resultados de evaluación no encontrados"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "user_id": usuario.id_usuario,
            "username": usuario.username,
            "resultado_evaluacion_inicial": {
                "competencia1": resultado_evaluacion_inicial.competencia_1,
                "competencia2": resultado_evaluacion_inicial.competencia_2,
                "competencia3": resultado_evaluacion_inicial.competencia_3,
                "competencia4": resultado_evaluacion_inicial.competencia_4,
                "competencia5": resultado_evaluacion_inicial.competencia_5,
            },
            "resultado_evaluacion_final": {
                "competencia1": resultado_evaluacion_final.competencia_1,
                "competencia2": resultado_evaluacion_final.competencia_2,
                "competencia3": resultado_evaluacion_final.competencia_3,
                "competencia4": resultado_evaluacion_final.competencia_4,
                "competencia5": resultado_evaluacion_final.competencia_5,
            }
        }

        return Response(data)

class AdminUsersListView(APIView):
    def get(self, request):
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        return Response({"users": serializer.data})

class AdminGenderSegmentationView(APIView):
    def get(self, request):
        gender_segmentation = Usuario.objects.values('genero').annotate(count=Count('genero'))
        return Response({"gender_segmentation": gender_segmentation})

class AdminAgeSegmentationView(APIView):
    def get(self, request):
        age_segmentation = Usuario.objects.annotate(
            age_group=Case(
                When(edad__range=(18, 24), then="18-24"),
                When(edad__range=(25, 34), then="25-34"),
                When(edad__range=(35, 44), then="35-44"),
                default="45+",
                output_field=IntegerField(),
            )
        ).values('age_group').annotate(count=Count('age_group'))
        return Response({"age_segmentation": age_segmentation})

class AdminNationalitySegmentationView(APIView):
    def get(self, request):
        nationality_segmentation = Usuario.objects.values('pais').annotate(count=Count('pais'))
        return Response({"nationality_segmentation": nationality_segmentation})

class AdminEducationSegmentationView(APIView):
    def get(self, request):
        education_segmentation = Usuario.objects.values('grado_ac').annotate(count=Count('grado_ac'))
        return Response({"education_segmentation": education_segmentation})

class UserProgressView(APIView):
    def get(self, request):
        return Response({"mensaje": "API de progreso del usuario"})

class UserProgressBarsView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        estadisticas = Estadisticas.objects.filter(id_usuario=id_usuario).first()

        if not estadisticas:
            return Response({"error": "Estadísticas no encontradas"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "id_estadistica": estadisticas.id_estadistica,
            "id_usuario": usuario.id_usuario,
            "actividades": estadisticas.actividades,
            "evidencias": estadisticas.evidencias,
            "progreso": estadisticas.progreso,
        }

        return Response(data)

class UserProgressBriefView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        progreso_actividades = ProgresoActividades.objects.filter(id_usuario=id_usuario).first()

        if not progreso_actividades:
            return Response({"error": "Progreso de actividades no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "id_progreso": progreso_actividades.id_progreso,
            "id_usuario": usuario.id_usuario,
            "actividad1": progreso_actividades.actividad1,
            "actividad2": progreso_actividades.actividad2,
            "actividad3": progreso_actividades.actividad3,
            "actividad4": progreso_actividades.actividad4,
        }

        return Response(data)

class UserProgressInitialEvaluationView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_inicial = ResultadoEvaluaciones.objects.filter(usuario=usuario, tipo_evaluacion="inicial").first()

        if not resultado_evaluacion_inicial:
            return Response({"error": "Resultados de evaluación inicial no encontrados"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "id_resultado": resultado_evaluacion_inicial.id_resultado,
            "id_evaluacion": resultado_evaluacion_inicial.id_evaluacion,
            "competencia1": resultado_evaluacion_inicial.competencia_1,
            "competencia2": resultado_evaluacion_inicial.competencia_2,
            "competencia3": resultado_evaluacion_inicial.competencia_3,
            "competencia4": resultado_evaluacion_inicial.competencia_4,
            "competencia5": resultado_evaluacion_inicial.competencia_5,
        }

        return Response(data)

class UserProgressFinalEvaluationView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_inicial = ResultadoEvaluaciones.objects.filter(usuario=usuario, tipo_evaluacion="inicial").first()
        resultado_evaluacion_final = ResultadoEvaluaciones.objects.filter(usuario=usuario, tipo_evaluacion="final").first()

        if not resultado_evaluacion_inicial or not resultado_evaluacion_final:
            return Response({"error": "Resultados de evaluación no encontrados"}, status=status.HTTP_404_NOT_FOUND)

        data = {
            "evaluacionInicial": {
                "id_resultado": resultado_evaluacion_inicial.id_resultado,
                "id_evaluacion": resultado_evaluacion_inicial.id_evaluacion,
                "competencia1": resultado_evaluacion_inicial.competencia_1,
                "competencia2": resultado_evaluacion_inicial.competencia_2,
                "competencia3": resultado_evaluacion_inicial.competencia_3,
                "competencia4": resultado_evaluacion_inicial.competencia_4,
                "competencia5": resultado_evaluacion_inicial.competencia_5,
            },
            "evaluacionFinal": {
                "id_resultado": resultado_evaluacion_final.id_resultado,
                "id_evaluacion": resultado_evaluacion_final.id_evaluacion,
                "competencia1": resultado_evaluacion_final.competencia_1,
                "competencia2": resultado_evaluacion_final.competencia_2,
                "competencia3": resultado_evaluacion_final.competencia_3,
                "competencia4": resultado_evaluacion_final.competencia_4,
                "competencia5": resultado_evaluacion_final.competencia_5,
            }
        }

        return Response(data)