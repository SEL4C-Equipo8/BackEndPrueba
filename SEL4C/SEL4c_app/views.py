
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Case, When, IntegerField, Count, Value
from django.db.models.functions import Cast
from .models import Usuario, Actividades, Modulos, EvidenciaModulos, Evaluaciones, ResultadoEvaluaciones, Estadisticas, ProgresoActividades, ProgresoUsuarios, Administrador, Preguntas, Respuestas
from django.shortcuts import get_object_or_404
from .serializers import UsuarioSerializer, ActividadesSerializer, ModulosSerializer, EvidenciaModulosSerializer, EvaluacionesSerializer, ResultadoEvaluacionesSerializer, EstadisticasSerializer, ProgresoActividadesSerializer, ProgresoUsuariosSerializer, AdministradorSerializer, PreguntasSerializer, RespuestasSerializer
from django.contrib.auth.hashers import check_password
from .forms import ModulesForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .swagger_params import *

#api/user/profile/<int:user_id>/
class UserProfileView(APIView):
    def get(self, request, user_id):
        usuario = get_object_or_404(Usuario, id_usuario=user_id)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    @updateUserProfile_swagger()
    def put(self, request, user_id):
        usuario = get_object_or_404(Usuario, id_usuario=user_id)
        serializer = UsuarioSerializer(usuario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Datos de perfil actualizados"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api/user/login/
# class UserLoginView(APIView):
#     def post(self, request):
#         # Obtener el correo electrónico y la contraseña de la solicitud POST
#         email = request.data.get('email')
#         password = request.data.get('contrasena')

#         try:
#             # Buscar al usuario por correo electrónico en la tabla personalizada
#             user = Usuario.objects.get(email=email)

#             # Verificar la contraseña
#             if user.contrasena == password:


#                 return Response({"message": "Inicio de sesión exitosa"}, status=status.HTTP_200_OK)
#             else:
#                 # La contraseña es incorrecta
#                 return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
#         except Usuario.DoesNotExist:
#             # El usuario no existe en la base de datos
#             return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)


#api/user/signup/
class UserSignupView(APIView):
    @signUp_swagger()
    def post(self, request, *args, **kwargs):
        # Obtenemos los datos del usuario desde la solicitud POST
        data = request.data

        # Serializamos los datos para validar y crear el usuario
        serializer = UsuarioSerializer(data=data)

        if serializer.is_valid():
            # Creamos el usuario
            usuario = serializer.save()

            # Devolvemos una respuesta exitosa
            response_data = {
                "message": "Usuario registrado con éxito", "id": usuario.id_usuario
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devolvemos los errores
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)


#api/user/evaluations/create
class CreateEvaluationView(APIView):
    @createEvaluation_swagger()
    def post(self, request):
        try:
            # Obtener los datos de la solicitud
            data = request.data
            tipo_evaluacion = data.get('tipo_evaluacion')
            imagen_env = request.FILES.get('imagen_env')
            
            # Crear una nueva instancia de Evaluaciones
            evaluacion = Evaluaciones.objects.create(
                tipo_evaluacion=tipo_evaluacion,
                imagen_env=imagen_env
            )
            
            return Response({"message": "Evaluación creada correctamente."}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"message": f"Error al crear la evaluación: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        evaluaciones = Evaluaciones.objects.all()
        serializer = EvaluacionesSerializer(evaluaciones, many=True)
        return Response(serializer.data)

from django.db.models import Sum, Avg
#api/user/evaluations/
class UploadEvaluationResultsView(APIView):
    @uploadEvaluation_swagger()
    def post(self, request):
        data = request.data
        try:
            idevaluacion = data.get('id_evaluacion')
            idusuario = data.get('id_usuario')  # Obtener el ID del usuario

            # Buscar el objeto Usuario correspondiente o devolver un error 404 si no existe
            usuario = Usuario.objects.filter(id_usuario=idusuario).first()

            if usuario is None:
                return Response({"message": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # Calcular las competencias
            respuestas = Respuestas.objects.filter(id_evaluacion=idevaluacion, id_usuario=idusuario)
            # Ordendar respuestas por id_pregunta ascendentemente
            respuestas = respuestas.order_by('id_pregunta')
            max_respuesta = 5  # El máximo valor posible para una respuesta

            competencia_2 = (respuestas.filter(id_pregunta__in=range(25, 31)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)
            competencia_3 = (respuestas.filter(id_pregunta__in=range(31, 38)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 7) * 100)
            competencia_4 = (respuestas.filter(id_pregunta__in=range(38, 44)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)
            competencia_5 = (respuestas.filter(id_pregunta__in=range(44, 50)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)

            competencia_1 = ((competencia_2 + competencia_3 + competencia_4 + competencia_5)/4)

            # Crear un nuevo objeto de evaluación y asignar el usuario
            evaluacion = ResultadoEvaluaciones.objects.create(
                id_evaluacion_id=idevaluacion,
                id_usuario_id=usuario.id_usuario,  # Asignar el usuario al objeto de evaluación
                competencia_1=competencia_1,
                competencia_2=competencia_2,
                competencia_3=competencia_3,
                competencia_4=competencia_4,
                competencia_5=competencia_5
            )
            
            return Response({"message": "Resultado subido."}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "Error al subir el resultado."}, status=status.HTTP_400_BAD_REQUEST)
    
    @uploadEvaluation_swagger()
    def put(self, request):
        data = request.data
        try:
            idevaluacion = data.get('id_evaluacion')
            idusuario = data.get('id_usuario')  # Obtener el ID del usuario

            # Buscar el objeto Usuario correspondiente o devolver un error 404 si no existe
            usuario = Usuario.objects.filter(id_usuario=idusuario).first()

            if usuario is None:
                return Response({"message": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

            # Calcular las competencias
            respuestas = Respuestas.objects.filter(id_evaluacion=idevaluacion, id_usuario=idusuario)
            # Ordendar respuestas por id_pregunta
            respuestas = respuestas.order_by('id_pregunta')
            max_respuesta = 5  # El máximo valor posible para una respuesta

            # competencia_1 = (respuestas.aggregate(promedio=Avg('respuesta'))['promedio'] / max_respuesta * 100
            #                  if respuestas.exists() 
            #                  else None)
            competencia_2 = (respuestas.filter(id_pregunta__in=range(25, 31)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)
            print (competencia_2)
            competencia_3 = (respuestas.filter(id_pregunta__in=range(31, 38)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 7) * 100)
            print (competencia_3)
            competencia_4 = (respuestas.filter(id_pregunta__in=range(38, 44)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)
            print (competencia_4)
            competencia_5 = (respuestas.filter(id_pregunta__in=range(44, 50)).aggregate(total=Sum('respuesta'))['total'] / (max_respuesta * 6) * 100)
            print (competencia_5)
            # Calcular competencia 1 a partir del promedio de las demas competencias
            competencia_1 = ((competencia_2 + competencia_3 + competencia_4 + competencia_5)/4)
            print (competencia_1)

            # Actualizar el objeto de evaluación si existe, o crear uno nuevo si no
            evaluacion, created = ResultadoEvaluaciones.objects.get_or_create(
                id_evaluacion_id=idevaluacion,
                id_usuario_id=usuario.id_usuario,  # Asignar el usuario al objeto de evaluación
                defaults={
                    'competencia_1': competencia_1,
                    'competencia_2': competencia_2,
                    'competencia_3': competencia_3,
                    'competencia_4': competencia_4,
                    'competencia_5': competencia_5
                }
            )

            if not created:
                # Si la evaluación ya existía, actualiza las competencias
                evaluacion.competencia_1 = competencia_1
                evaluacion.competencia_2 = competencia_2
                evaluacion.competencia_3 = competencia_3
                evaluacion.competencia_4 = competencia_4
                evaluacion.competencia_5 = competencia_5
                evaluacion.save()

            return Response({"message": "Resultado actualizado."}, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Error al actualizar el resultado."}, status=status.HTTP_400_BAD_REQUEST)



#api/user/evidences/
class UploadModuleEvidenceView(APIView):
    @uploadModuleEvidence_swagger()
    def post(self, request):
        # Obtén los datos de la solicitud JSON
        data = request.data

        # Crea una instancia del serializador con los datos de la solicitud
        serializer = EvidenciaModulosSerializer(data=data)

        if serializer.is_valid():
            # Guarda la evidencia en la base de datos
            serializer.save()
            return Response({"message": "Actividad subida exitosamente"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api/admin/activities/all/
class ActivityListView(APIView):
    def get(self, request):
        actividades = Actividades.objects.all()
        serializer = ActividadesSerializer(actividades, many=True)
        return Response(serializer.data)

#api/admin/activities/<int:id_actividad>/
class ActivityDetailView(APIView):
    def get(self, request, id_actividad):
        actividad = get_object_or_404(Actividades, id_actividad=id_actividad)
        serializer = ActividadesSerializer(actividad)
        return Response(serializer.data)
    @updateActivity_swagger()
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

#api/admin/activities/
class ActivityCreateView(APIView):
    @activityCreateView_swagger()
    def post(self, request):
        serializer = ActividadesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Actividad publicada con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api/admin/activity/<int:id_actividad>/module/all/
class ModuleListView(APIView):
    def get(self, request, id_actividad):
        # Obtén todos los módulos que pertenecen a la actividad especificada
        modulos = Modulos.objects.filter(id_actividad=id_actividad)
        serializer = ModulosSerializer(modulos, many=True)
        return Response(serializer.data)

#api/admin/activity/<int:id_actividad>/module/<int:id_modulo>/
class ModuleDetailView(APIView):
    def get(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        serializer = ModulosSerializer(modulo)
        if request.accepted_renderer.format == 'html':
            # Si la solicitud acepta formato HTML, renderiza el formulario
            form = ModulesForm(instance=modulo)
            return render(request, 'form.html', {'form': form, 'serializer': serializer.data})
        # Si no, responde con JSON
        return Response(serializer.data)
    @updateModule_swagger()
    def put(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        serializer = ModulosSerializer(modulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Modulo actualizado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        modulo.delete()
        return Response({"message": "Módulo eliminado con éxito"})

'''
def ModuleUpdateView(request, id_actividad, id_modulo):
    # Obtén la instancia del módulo que deseas actualizar
    modulo = get_object_or_404(Modulos, id_modulo=id_modulo)

    if request.method == 'POST':
        # Si el formulario se ha enviado con datos, procesa el formulario
        form = ModulesForm(request.POST, instance=modulo)

        if form.is_valid():
            # Guarda los cambios en el módulo
            form.save()
        return HttpResponse('<script>alert("Modulo Actualizado");window.location.href="/api/admin/activity/'+str(id_actividad)+'/module/'+str(id_modulo)+'/update/";</script>')

    else:
        # Si no se ha enviado el formulario, crea una instancia del formulario con los datos actuales del módulo
        form = ModulesForm(instance=modulo)

    return render(request, 'formUpdate.html', {'form': form})
'''

class ModuleUpdateView(APIView):
    @updateModule_swagger()
    def put(self, request, id_actividad, id_modulo):
        modulo = get_object_or_404(Modulos, id_modulo=id_modulo, id_actividad=id_actividad)
        serializer = ModulosSerializer(modulo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Modulo actualizado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api/admin/activity/<int:id_actividad>/module/  
#@csrf_exempt
'''
def ModuleCreateView(request, id_actividad):
    form = ModulesForm()
    if request.method == 'POST':
        form = ModulesForm(request.POST)
        if form.is_valid():
            titulo_mod = form.cleaned_data['titulo_mod']
            instrucciones = form.cleaned_data['instrucciones']
            imagen_mod = form.cleaned_data['imagen_mod']
            tipo_multimedia = form.cleaned_data['tipo_multimedia']
            modulo = Modulos(id_actividad_id=id_actividad, titulo_mod=titulo_mod, instrucciones=instrucciones, imagen_mod=imagen_mod, tipo_multimedia=tipo_multimedia)
            modulo.save()
            messages.success(request, 'Modulo creado')
            form = ModulesForm()
            #return render(request, 'form.html', {'form': form})
        # HTTP alert and redirect to the same page
        return HttpResponse('<script>alert("Modulo creado");window.location.href="/api/admin/activity/'+str(id_actividad)+'/module/create/";</script>')
    #else:
        #form = ModulesForm()
    return render(request, 'form.html', {'form': form})
    '''

class ModuleCreateView(APIView):
    @createModule_swagger()
    def post(self, request, id_actividad):
        # Intenta obtener la Actividad con el id_actividad proporcionado
        try:
            actividad = Actividades.objects.get(pk=id_actividad)
        except Actividades.DoesNotExist:
            return Response({'error': 'Actividad no encontrada'}, status=status.HTTP_404_NOT_FOUND)

        # Modifica el request.data para agregar el id_actividad (asegúrate de hacer una copia para no modificar el request original)
        data = request.data.copy()
        data['id_actividad'] = actividad.id_actividad
        
        serializer = ModulosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Modulo publicado con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api/admin/login/
class AdminLoginView(APIView):
    @adminLogin_swagger()
    def post(self, request):
        # Obtener el correo electrónico y la contraseña de la solicitud POST
        correo = request.data.get('correo')
        contrasena = request.data.get('contrasena')
        try:
            # Buscar al administrador por correo electrónico en la tabla Administrador
            admin = Administrador.objects.get(correo=correo)
            print (admin)
            # Verificar la contraseña
            if admin.contrasena == contrasena:
                # Definicion de cookies
                request.session.flush()
                response = redirect('whoami')
                response.set_cookie("id_admin", str(admin.pk))
                #return Response({"message": "Inicio de sesión exitosa", "Cookie":cookie_value}, status=status.HTTP_200_OK)
                return response
            else:
                # La contraseña es incorrecta
                return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)
        except Administrador.DoesNotExist:
            # El administrador no existe en la base de datos
            return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

#### AUXILIARES PARA LOGIN ADMIN Y COOKIES
class AdminSignupView(APIView):
    def post(self, request, *args, **kwargs):
        # Obtenemos los datos del usuario desde la solicitud POST
        data = request.data

        # Serializamos los datos para validar y crear el usuario
        serializer = AdministradorSerializer(data=data)

        if serializer.is_valid():
            # Creamos el usuario
            administrador = serializer.save()

            # Devolvemos una respuesta exitosa
            response_data = {
                "message": "Administrador registrado con éxito"
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            # Si los datos no son válidos, devolvemos los errores
            errors = serializer.errors
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
def whoami(request):
    context = {}
    print(request.COOKIES)
    if 'id_admin' in request.COOKIES:
        admin = request.COOKIES['id_admin']
        user = Administrador.objects.get(id_admin=admin)
        #context['message'] = 'Eres el usuario admin ' + str(admin)
        context['id_admin'] = admin

        return HttpResponse('<script>alert("Eres el admin '+str(admin)+'");window.location.href="/api/admin/";</script>')
    else:
        return HttpResponse('<script>alert("No hay usuario admin");window.location.href="/api/admin/login/";</script>')
    
class AdminLogoutView(APIView):
    def get(self, request):
        request.session.flush()
        return HttpResponse('<script>alert("Sesion cerrada");window.location.href="/api/admin/login/";</script>')
    #####################################################################################################################
    
#api/admin/
class AdminListView(APIView):
    def get(self, request):
        administradores = Administrador.objects.all()
        serializer = AdministradorSerializer(administradores, many=True)
        return Response(serializer.data)
    @adminLogin_swagger()
    def post(self, request):
        data = request.data
        serializer = AdministradorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Administrador creado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api/admin/<int:id_admin>/
class AdminDetailView(APIView):
    def get(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        serializer = AdministradorSerializer(admin)
        return Response(serializer.data)
    @detailAdmin_swagger()
    def put(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        serializer = AdministradorSerializer(admin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"mensaje": "Administrador actualizado exitosamente"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @detailAdmin_swagger()
    def delete(self, request, id_admin):
        admin = get_object_or_404(Administrador, id_admin=id_admin)
        admin.delete()
        return Response({"mensaje": "Administrador eliminado exitosamente"})

#api/progress/
class AdminDashboardView(APIView):
    def get(self, request):
        return Response({"mensaje": "Panel de control del administrador"})

#api/admin/personalProgress/<int:user_id>/
class AdminPersonalProgressView(APIView):
    def get(self, request, user_id):
        try:
            usuario = Usuario.objects.get(id_usuario=user_id)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_inicial = ResultadoEvaluaciones.objects.filter(id_usuario=usuario, id_evaluacion=1).first()
        resultado_evaluacion_final = ResultadoEvaluaciones.objects.filter(id_usuario=usuario, id_evaluacion=2).first()

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

#api/admin/users/
class AdminUsersListView(APIView):
    def get(self, request):
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)
        return Response({"users": serializer.data})

#api/admin/segmentation/gender/
class AdminGenderSegmentationView(APIView):
    def get(self, request):
        gender_segmentation = Usuario.objects.values('genero').annotate(count=Count('genero'))
        return Response({"gender_segmentation": gender_segmentation})

#api/segmentation/admin/age/
class AdminAgeSegmentationView(APIView):
    def get(self, request):
        age_segmentation = Usuario.objects.annotate(
            age_group=Case(
                When(edad__range=(15, 20), then=Cast(Value("15-20"), output_field=IntegerField())),
                When(edad__range=(21, 25), then=Cast(Value("21-25"), output_field=IntegerField())),
                When(edad__range=(26, 30), then=Cast(Value("26-30"), output_field=IntegerField())),
                When(edad__range=(31, 35), then=Cast(Value("31-35"), output_field=IntegerField())),
                When(edad__range=(36, 40), then=Cast(Value("36-40"), output_field=IntegerField())),
                default=Cast(Value("45+"), output_field=IntegerField()),
                output_field=IntegerField(),
            )
        ).values('age_group').annotate(count=Count('age_group'))
        return Response({"age_segmentation": age_segmentation})

#api/segmentation/admin/nationality/
class AdminNationalitySegmentationView(APIView):
    def get(self, request):
        nationality_segmentation = Usuario.objects.values('pais').annotate(count=Count('pais'))
        return Response({"nationality_segmentation": nationality_segmentation})

#api/segmentation/admin/education/
class AdminEducationSegmentationView(APIView):
    def get(self, request):
        education_segmentation = Usuario.objects.values('grado_ac').annotate(count=Count('grado_ac'))
        return Response({"education_segmentation": education_segmentation})

#api/user/progress/bars/<int:id_usuario>/
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
    @graficaBarras_swagger()
    def put(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        estadisticas = Estadisticas.objects.filter(id_usuario=id_usuario).first()

        if not estadisticas:
            return Response({"error": "Estadísticas no encontradas"}, status=status.HTTP_404_NOT_FOUND)

        # Actualiza los datos de progreso con los datos proporcionados en la solicitud PUT
        # Asumiendo que la solicitud PUT contiene un JSON con los datos a actualizar
        # Ejemplo de solicitud PUT JSON: {"actividades": 10, "evidencias": 5, "progreso": 80}
        if 'actividades' in request.data:
            estadisticas.actividades = request.data['actividades']
        if 'evidencias' in request.data:
            estadisticas.evidencias = request.data['evidencias']
        if 'progreso' in request.data:
            estadisticas.progreso = request.data['progreso']

        estadisticas.save()  # Guardar los cambios en la base de datos

        data = {
            "id_estadistica": estadisticas.id_estadistica,
            "id_usuario": usuario.id_usuario,
            "actividades": estadisticas.actividades,
            "evidencias": estadisticas.evidencias,
            "progreso": estadisticas.progreso,
        }

        return Response(data)
    
#api/user/progress/activities/<int:id_usuario>/
class UserProgressActivtiesView(APIView):
    @progresoActividades_swagger()
    def post(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data

        # Validación de datos
        if 'actividad1' not in data or 'actividad2' not in data or 'actividad3' not in data or 'actividad4' not in data:
            return Response({"error": "Los campos de actividad deben estar presentes"}, status=status.HTTP_400_BAD_REQUEST)

        actividad1 = data.get('actividad1')
        actividad2 = data.get('actividad2')
        actividad3 = data.get('actividad3')
        actividad4 = data.get('actividad4')

        # Crear o actualizar el progreso de actividades
        progreso_actividades, created = ProgresoActividades.objects.update_or_create(
            id_usuario=usuario,
            defaults={
                "actividad1": actividad1,
                "actividad2": actividad2,
                "actividad3": actividad3,
                "actividad4": actividad4,
            }
        )

        return Response({"message": "Progreso de actividades actualizado exitosamente"}, status=status.HTTP_200_OK)
    @actualizarProgresoActividades_swagger()
    def put(self, request, id_usuario):
        return self.post(request, id_usuario)

#api/user/progress/brief/<int:id_usuario>/
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
    @actualizarProgresoActividades_swagger()
    def put(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        progreso_actividades = ProgresoActividades.objects.filter(id_usuario=id_usuario).first()

        if not progreso_actividades:
            return Response({"error": "Progreso de actividades no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Get the activity name and new value from the request data
        activity_name = request.data.get("activity_name")
        new_value = request.data.get("new_value")

        # Check if the activity_name is valid and update the corresponding field
        if activity_name in ["actividad1", "actividad2", "actividad3", "actividad4"]:
            setattr(progreso_actividades, activity_name, new_value)
            progreso_actividades.save()
            serializer = ProgresoActividadesSerializer(progreso_actividades)
            return Response(serializer.data)
        else:
            return Response({"error": "Actividad no válida"}, status=status.HTTP_400_BAD_REQUEST)

#api/user/progress/initialEvaluation/<int:id_usuario/
class UserProgressInitialEvaluationView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_inicial = ResultadoEvaluaciones.objects.filter(id_usuario=id_usuario, id_evaluacion=1).first()

        if not resultado_evaluacion_inicial:
            return Response({"error": "Resultados de evaluación inicial no encontrados"}, status=status.HTTP_404_NOT_FOUND)

        resultado = str(resultado_evaluacion_inicial.id_resultado)
        evaluacion = str(resultado_evaluacion_inicial.id_evaluacion)
        competencia1 = str(resultado_evaluacion_inicial.competencia_1)
        competencia2 = str(resultado_evaluacion_inicial.competencia_2)
        competencia3 = str(resultado_evaluacion_inicial.competencia_3)
        competencia4 = str(resultado_evaluacion_inicial.competencia_4)
        competencia5 = str(resultado_evaluacion_inicial.competencia_5)

        data = {
            "id_resultado": resultado,
            "id_evaluacion": evaluacion,
            "competencia1": competencia1,
            "competencia2": competencia2,
            "competencia3": competencia3,
            "competencia4": competencia4,
            "competencia5": competencia5,
        }

        return Response(data)

#api/user/progress/finalEvaluation/<int:id_usuario/
class UserProgressFinalEvaluationView(APIView):
    def get(self, request, id_usuario):
        try:
            usuario = Usuario.objects.get(id_usuario=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": "Usuario no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        resultado_evaluacion_final = ResultadoEvaluaciones.objects.filter(id_usuario=id_usuario, id_evaluacion=2).first()

        if not resultado_evaluacion_final:
            return Response({"error": "Resultados de evaluación final no encontrados"}, status=status.HTTP_404_NOT_FOUND)

        resultado = str(resultado_evaluacion_final.id_resultado)
        evaluacion = str(resultado_evaluacion_final.id_evaluacion)
        competencia1 = str(resultado_evaluacion_final.competencia_1)
        competencia2 = str(resultado_evaluacion_final.competencia_2)
        competencia3 = str(resultado_evaluacion_final.competencia_3)
        competencia4 = str(resultado_evaluacion_final.competencia_4)
        competencia5 = str(resultado_evaluacion_final.competencia_5)

        data = {
            "id_resultado": resultado,
            "id_evaluacion": evaluacion,
            "competencia1": competencia1,
            "competencia2": competencia2,
            "competencia3": competencia3,
            "competencia4": competencia4,
            "competencia5": competencia5,
        }

        return Response(data)
    
#api/admin/estadisticas/create/
class EstadisticasCreateView(APIView):
    @publicarEstadisticas_swagger()
    def post(self, request):
        # Obtén los datos del cuerpo de la solicitud JSON
        data = request.data

        # Serializa los datos para validar y crear una nueva estadística
        serializer = EstadisticasSerializer(data=data)

        if serializer.is_valid():
            # Guarda la nueva estadística en la base de datos
            serializer.save()
            return Response({"message": "Estadísticas creadas exitosamente"}, status=status.HTTP_201_CREATED)
        else:
            # Si la validación falla, devuelve los errores
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#api/user/progress/user/<int:id_usuario>/
class UserProgressView(APIView):
    def get_object(self, id_usuario):
        try:
            return ProgresoUsuarios.objects.get(id_usuario=id_usuario)
        except ProgresoUsuarios.DoesNotExist:
            return None
        
    def get(self, request, id_usuario):
        # Recuperar todos los registros de ProgresoUsuarios con el id_usuario proporcionado
        progresos_usuario = ProgresoUsuarios.objects.filter(id_usuario=id_usuario)
        
        # Verificar si se encontraron registros
        if progresos_usuario.exists():
            serializer = ProgresoUsuariosSerializer(progresos_usuario, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": f"No se encontraron registros de progreso para el usuario con ID {id_usuario}"}, status=status.HTTP_404_NOT_FOUND)
    @actualizarProgresoUsuario_swagger()
    def post(self, request, id_usuario):
        try:
            # Verifica si el usuario existe antes de crear el registro de progreso
            usuario = Usuario.objects.get(pk=id_usuario)
        except Usuario.DoesNotExist:
            return Response({"error": f"El usuario con ID {id_usuario} no existe"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProgresoUsuariosSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(id_usuario=usuario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @actualizarProgresoUsuario_swagger()
    def put(self, request, id_usuario):
        id_actividad = request.data.get("id_actividad")
        id_modulo = request.data.get("id_modulo")
        estado_actividad = request.data.get("estado_actividad")
        estado_modulo = request.data.get("estado_modulo")

        try:
            progreso_usuario = ProgresoUsuarios.objects.get(
                id_usuario=id_usuario,
                id_actividad=id_actividad,
                id_modulo=id_modulo
            )

            # Actualiza los campos específicos
            progreso_usuario.estado_actividad = estado_actividad
            progreso_usuario.estado_modulo = estado_modulo
            progreso_usuario.save()

            serializer = ProgresoUsuariosSerializer(progreso_usuario)
            return Response(serializer.data)
        except ProgresoUsuarios.DoesNotExist:
            return Response({"error": f"No se encontró un registro de progreso con los criterios proporcionados"}, status=status.HTTP_404_NOT_FOUND)
    


from django.contrib.auth import authenticate, login
#from django.contrib.auth.models import Usuario
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from .serializers import TokenSerializer

# Get the JWT settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

class UserLoginView(APIView):
    """
    POST authentication/login/
    """

    # Esta clase de permiso anulará la configuración global de permisos
    permission_classes = (permissions.AllowAny,)
    @loginUsuario_swagger()
    def post(self, request, *args, **kwargs):
        email = request.data.get("email", "")
        contrasena = request.data.get("contrasena", "")
        
        # Aquí debes realizar tu propia lógica de autenticación
        try:
            user = Usuario.objects.get(email=email)
            if user.contrasena == contrasena:
                id_usuario = user.id_usuario
                # Aquí puedes generar un token como lo estabas haciendo
                serializer = TokenSerializer(data={
                    "token": jwt_encode_handler(
                        jwt_payload_handler(user)
                    )})
                serializer.is_valid()
                return Response({"message": "Credenciales válidas", "token": serializer.data, "id": id_usuario} )
        except Usuario.DoesNotExist:
            pass

        return Response(status=status.HTTP_401_UNAUTHORIZED)

class UserLogout(APIView):
    #Logout para usuarios
    def get(self, request, format=None):
        # simplemente elimina la sesión actual del usuario
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
    
#api/preguntas/all/
class PreguntasListView(APIView):
    def get(self, request):
        preguntas = Preguntas.objects.all()
        serializer = PreguntasSerializer(preguntas, many=True)
        return Response(serializer.data)
    @publicarPreguntas_swagger()
    def post(self, request):
        preguntas_data = request.data  # Obtenemos los datos JSON enviados en la solicitud
        preguntas_con_id = []  # Aquí almacenaremos las preguntas con ID asignado

        for pregunta_data in preguntas_data:
            # Creamos una nueva pregunta en la base de datos y asignamos un ID automáticamente
            nueva_pregunta = Preguntas.objects.create(contenido=pregunta_data['contenido'])
            
            # Serializamos la pregunta recién creada
            serializer = PreguntasSerializer(nueva_pregunta)
            preguntas_con_id.append(serializer.data)

        return Response(preguntas_con_id, status=status.HTTP_201_CREATED)


#api/preguntas/<int:id_pregunta>/
class PreguntasDetailView(APIView):
    def get(self, request, id_pregunta):
        pregunta = get_object_or_404(Preguntas, id_pregunta=id_pregunta)
        serializer =PreguntasSerializer(pregunta)
        return Response(serializer.data)
    @publicarPreguntas_swagger()
    def post(self, request):
        serializer = PreguntasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Pregunta publicada con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @actualizarPregunta_swagger()
    def put(self, request, id_pregunta):
        pregunta = get_object_or_404(Preguntas, id_pregunta=id_pregunta)
        serializer = PreguntasSerializer(pregunta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Pregunta actualizada con éxito"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    @eliminarPregunta_swagger()
    def delete(self, request, id_pregunta):
        pregunta = get_object_or_404(Preguntas, id_pregunta=id_pregunta)
        pregunta.delete()
        return Response({"message": "Actividad eliminada con éxito"})
    
#api/respuestas/<int:id_usuario>/<int:id_evaluacion>/ 
class RespuestasDetailView(APIView):
    def get(self, request, id_usuario, id_evaluacion):
        respuestas = Respuestas.objects.filter(id_usuario=id_usuario, id_evaluacion=id_evaluacion)
        serializer = RespuestasSerializer(respuestas, many=True)
        return Response(serializer.data)
    # Función para documentación
    @enviarRespuestas_swagger()
    def post(self, request, id_usuario, id_evaluacion):
            try:
                respuestas_data = request.data  # Obtenemos los datos JSON enviados en la solicitud
                respuestas_creadas = []

                # Obtener el id_usuario de la tabla Usuario
                user = Usuario.objects.get(id_usuario=id_usuario)
                # Obtener el id_evaluacion de la tabla Evaluaciones
                evaluacion = Evaluaciones.objects.get(id_evaluacion=id_evaluacion)

                for respuesta_data in respuestas_data:
                    id_pregunta_json = respuesta_data.get('id')
                    respuesta_valor = respuesta_data.get('respuesta')
                    pregunta = Preguntas.objects.get(id_pregunta=id_pregunta_json)

                    # Verificar si ya existe una respuesta para esta pregunta, usuario y evaluación
                    respuesta, created = Respuestas.objects.get_or_create(
                        id_evaluacion=evaluacion,
                        id_usuario=user,
                        id_pregunta=pregunta,
                        defaults={'respuesta': respuesta_valor}
                    )

                    if not created:
                        # Si ya existe, actualizamos la respuesta
                        respuesta.respuesta = respuesta_valor
                        respuesta.save()

                    respuestas_creadas.append({"id_respuesta": respuesta.id_respuesta})

                return Response({"message": "Respuestas creadas/actualizadas exitosamente.", "respuestas_creadas": respuestas_creadas}, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
'''
    def post(self, request, id_usuario, id_evaluacion):
        try:
            respuestas_data = request.data  # Obtenemos los datos JSON enviados en la solicitud
            respuestas_creadas = []
            #Obtener el id_usuario de la tabla Usuario
            user = Usuario.objects.get(id_usuario=id_usuario)
            idUsuario = user.id_usuario
            #Obtener el id_evaluacion de la tabla Evaluaciones
            evaluacion = Evaluaciones.objects.get(id_evaluacion=id_evaluacion)
            id_evaluacion = evaluacion.id_evaluacion
            print (idUsuario, id_evaluacion)
            for respuesta_data in respuestas_data:
                id_pregunta_json = respuesta_data.get('id')
                respuesta_valor = respuesta_data.get('respuesta')
                pregunta = Preguntas.objects.get(id_pregunta=id_pregunta_json)
                # Crear una nueva respuesta en la base de datos y asignar un ID automáticamente
                respuesta = Respuestas(id_evaluacion=evaluacion, id_usuario=user, id_pregunta=pregunta, respuesta=respuesta_valor)
                respuesta.save()
                respuestas_creadas.append({"id_respuesta": respuesta.id_respuesta})

            return Response({"message": "Respuestas creadas exitosamente.", "respuestas_creadas": respuestas_creadas}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_usuario, id_evaluacion, id_respuesta):
        respuesta = get_object_or_404(Respuestas, id_usuario=id_usuario, id_evaluacion=id_evaluacion, id_respuesta=id_respuesta)
        respuesta.delete()
        return Response({"message": "Respuesta eliminada con éxito."})
'''
    

from rest_framework import permissions
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(
    title="API de SEL4C",
    public=True,
    permission_classes=[permissions.AllowAny],  # Puedes cambiar esto según tus necesidades de autenticación
)