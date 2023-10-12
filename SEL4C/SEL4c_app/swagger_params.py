from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Swagger Parameters

# User
#UserLoginView
def loginUsuario_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email'),
                'contrasena': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['email', 'contrasena']
        ),
        responses={
            201: 'Credenciales válidas',
            400: 'Bad Request'
        }
    )
#api/user/profile/<int:user_id>/
def updateUserProfile_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electrónico'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
                'photo': openapi.Schema(type=openapi.TYPE_FILE, description='Foto de perfil'),
                'grado_ac': openapi.Schema(type=openapi.TYPE_STRING, description='Grado académico'),
                'institucion': openapi.Schema(type=openapi.TYPE_STRING, description='Institución'),
                'genero': openapi.Schema(type=openapi.TYPE_STRING, description='Género'),
                'edad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Edad'),
                'pais': openapi.Schema(type=openapi.TYPE_STRING, description='País'),
                'disciplina': openapi.Schema(type=openapi.TYPE_STRING, description='Disciplina'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['username', 'password', 'email', 'photo', 'grado_ac', 'institucion', 'genero', 'edad', 'pais', 'disciplina']
        ),
        responses={
            201: 'Datos de perfil actualizados',
            400: 'Bad Request'
        }
    )
def signUp_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Nombre de usuario'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Correo electrónico'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Contraseña'),
                'photo': openapi.Schema(type=openapi.TYPE_FILE, description='Foto de perfil'),
                'grado_ac': openapi.Schema(type=openapi.TYPE_STRING, description='Grado académico'),
                'institucion': openapi.Schema(type=openapi.TYPE_STRING, description='Institución'),
                'genero': openapi.Schema(type=openapi.TYPE_STRING, description='Género'),
                'edad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Edad'),
                'pais': openapi.Schema(type=openapi.TYPE_STRING, description='País'),
                'disciplina': openapi.Schema(type=openapi.TYPE_STRING, description='Disciplina'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['username', 'password', 'email', 'photo', 'grado_ac', 'institucion', 'genero', 'edad', 'pais', 'disciplina']
        ),
        responses={
            201: 'Usuario registrado con éxito',
            400: 'Bad Request'
        }
    )
#api/user/evaluations/create
def createEvaluation_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'tipo_evaluacion': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo evaluación'),
                'image_env': openapi.Schema(type=openapi.TYPE_FILE, description='Imagen evaluación'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['tipo_evaluacion', 'image_env']
        ),
        responses={
            201: 'Evaluación creada correctamente',
            400: 'Bad Request'
        }
    )
#api/user/evaluations/
def uploadEvaluation_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'id_evaluacion': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID evaluación'),
                'competencia_1': openapi.Schema(type=openapi.TYPE_INTEGER, description='Competencia 1'),
                'competencia_2': openapi.Schema(type=openapi.TYPE_INTEGER, description='Competencia 2'),
                'competencia_3': openapi.Schema(type=openapi.TYPE_INTEGER, description='Competencia 3'),
                'competencia_4': openapi.Schema(type=openapi.TYPE_INTEGER, description='Competencia 4'),
                'competencia_5': openapi.Schema(type=openapi.TYPE_INTEGER, description='Competencia 5'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_usuario', 'id_evaluacion', 'competencia_1', 'competencia_2', 'competencia_3', 'competencia_4', 'competencia_5']
        ),
        responses={
            201: 'Resultado subido',
            400: 'Bad Request'
        }
    )
#api/user/evidences/
def uploadModuleEvidence_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_respuesta': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID respuesta'),
                'id_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID módulo'),
                'archivo_res': openapi.Schema(type=openapi.TYPE_FILE, description='Archivo respuesta'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_respuesta', 'id_modulo', 'archivo_res']
        ),
        responses={
            201: 'Actividad subida exitosamente',
            400: 'Bad Request'
        }
    )
#api/user/progress/bars/<int:id_usuario>/
def graficaProgresoActividades_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'actividad1': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 1'),
                'actividad2': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 2'),
                'actividad3': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 3'),
                'actividad4': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 4'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_usuario', 'actividad1', 'actividad2', 'actividad3', 'actividad4']
        ),
        responses={
            201: 'Progreso de actividades actualizado exitosamente',
            400: 'Bad Request'
        }
    )
#api/user/progress/bars/<int:id_usuario>/
def graficaBarras_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_estadistica': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID estadistica'),
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'actividades': openapi.Schema(type=openapi.TYPE_INTEGER, description='Actividades'),
                'evidencias': openapi.Schema(type=openapi.TYPE_INTEGER, description='Evidencias'),
                'progreso': openapi.Schema(type=openapi.TYPE_INTEGER, description='Progreso'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_estadistica', 'id_usuario', 'actividades', 'evidencias', 'progreso']
        ),
        responses={
            201: 'Estadísticas publicadas',
            400: 'Bad Request'
        }
    )
#api/user/progress/activities/<int:id_usuario>/ 
def progresoActividades_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'actividad1': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 1'),
                'actividad2': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 2'),
                'actividad3': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 3'),
                'actividad4': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 4'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_progreso', 'id_usuario', 'actividad1', 'actividad2', 'actividad3', 'actividad4']
        ),
        responses={
            201: 'Progreso de actividades actualizado exitosamente',
            400: 'Bad Request'
        }
    )
#api/user/progress/activities/<int:id_usuario>/ -> PUT
#api/user/progress/brief/<int:id_usuario>/
def actualizarProgresoActividades_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_progreso': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID progreso'),
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'actividad1': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 1'),
                'actividad2': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 2'),
                'actividad3': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 3'),
                'actividad4': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Actividad 4'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_progreso', 'id_usuario', 'actividad1', 'actividad2', 'actividad3', 'actividad4']
        ),
        responses={
            201: 'Progreso de actividades actualizado exitosamente',
            400: 'Bad Request'
        }
    )
#api/admin/estadisticas/create/
def publicarEstadisticas_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'actividades': openapi.Schema(type=openapi.TYPE_INTEGER, description='Actividades'),
                'evidencias': openapi.Schema(type=openapi.TYPE_INTEGER, description='Evidencias'),
                'progreso': openapi.Schema(type=openapi.TYPE_INTEGER, description='Progreso'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_usuario', 'actividades', 'evidencias', 'progreso']
        ),
        responses={
            201: 'Estadísticas publicadas',
            400: 'Bad Request'
        }
    )
#api/user/progress/user/<int:id_usuario>/ -> POST
def actualizarProgresoUsuario_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'id_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID actividad'),
                'id_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID modulo'),
                'estado_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estado actividad'),
                'estado_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estado módulo'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_usuario', 'id_actividad', 'id_modulo', 'estado_actividad', 'estado_modulo']
        ),
        responses={
            201: 'Progreso usuario',
            400: 'Bad Request'
        }
    )
#api/user/progress/user/<int:id_usuario>/ -> PUT
def actualizarProgresoUsuario_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_progreso_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID progreso usuario'),
                'id_usuario': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID usuario'),
                'id_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID actividad'),
                'id_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID modulo'),
                'estado_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estado actividad'),
                'estado_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='Estado módulo'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_progreso_usuario', 'id_usuario', 'id_actividad', 'id_modulo', 'estado_actividad', 'estado_modulo']
        ),
        responses={
            201: 'Progreso usuario actualizado',
            400: 'Bad Request'
        }
    )

############################################################
# ADMIN

#api/admin/activities/<int:id_actividad>/
def updateActivity_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID actividad'),
                'titulo': openapi.Schema(type=openapi.TYPE_STRING, description='Título'),
                'imagen': openapi.Schema(type=openapi.TYPE_FILE, description='Imagen'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_actividad', 'titulo', 'imagen', 'descripcion']
        ),
        responses={
            201: 'Actividad actualizada con éxito',
            400: 'Bad Request'
        }
    )
#api/admin/activities/
def activityCreateView_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'titulo': openapi.Schema(type=openapi.TYPE_STRING, description='Título'),
                'imagen': openapi.Schema(type=openapi.TYPE_FILE, description='Imagen'),
                'descripcion': openapi.Schema(type=openapi.TYPE_STRING, description='Descripcion'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['titulo', 'imagen', 'descripcion']
        ),
        responses={
            201: 'Actividad publicada con éxito',
            400: 'Bad Request'
        }
    )
#api/admin/activity/<int:id_actividad>/module/<int:id_modulo>/
def updateModule_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_modulo': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID módulo'),
                'id_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID actividad'),
                'titulo_mod': openapi.Schema(type=openapi.TYPE_STRING, description='Título módulo'),
                'instrucciones': openapi.Schema(type=openapi.TYPE_STRING, description='Instrucciones'),
                'image_mod': openapi.Schema(type=openapi.TYPE_FILE, description='Imagen módulo'),
                'tipo_multimedia': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo multimedia'),
            },
            required=['id_modulo', 'id_actividad', 'titulo_mod', 'instrucciones', 'image_mod', 'tipo_multimedia']
        ),
        responses={
            201: 'Módulo actualizado con éxito',
            400: 'Bad Request'
        }
    )
#ModuleCreateView
def createModule_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_actividad': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID actividad'),
                'titulo_mod': openapi.Schema(type=openapi.TYPE_STRING, description='Título módulo'),
                'instrucciones': openapi.Schema(type=openapi.TYPE_STRING, description='Instrucciones'),
                'image_mod': openapi.Schema(type=openapi.TYPE_FILE, description='Imagen módulo'),
                'tipo_multimedia': openapi.Schema(type=openapi.TYPE_STRING, description='Tipo multimedia'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_actividad', 'titulo_mod', 'instrucciones', 'image_mod', 'tipo_multimedia']
        ),
        responses={
            201: 'Módulo publicado con éxito',
            400: 'Bad Request'
        }
    )
#api/admin/login/
def adminLogin_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'correo': openapi.Schema(type=openapi.TYPE_STRING, description='correo'),
                'contrasena': openapi.Schema(type=openapi.TYPE_STRING, description='contrasena'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['correo', 'contrasena']
        ),
        responses={
            201: 'Administrador registrado con éxito',
            400: 'Bad Request'
        }
    )
#api/admin/<int:id_admin>/
def detailAdmin_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'id_admin': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID admin'),
                'correo': openapi.Schema(type=openapi.TYPE_STRING, description='correo'),
                'contrasena': openapi.Schema(type=openapi.TYPE_STRING, description='contrasena'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['id_admin', 'correo', 'contrasena']
        ),
        responses={
            201: 'Administrador registrado con éxito',
            400: 'Bad Request'
        }
    )

############################################################
# Preguntas

#api/preguntas/all/
#api/preguntas/<int:id_pregunta>/
def publicarPreguntas_swagger():
    return swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'contenido': openapi.Schema(type=openapi.TYPE_STRING, description='Contenido'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['contenido']
        ),
        responses={
            201: 'Pregunta creada',
            400: 'Bad Request'
        }
    )
#api/preguntas/<int:id_pregunta>/ -> PUT
def actualizarPregunta_swagger():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id_pregunta',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID de la pregunta a actualizar',
                required=True
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'contenido': openapi.Schema(type=openapi.TYPE_STRING, description='Nuevo contenido de la pregunta'),
                # Agrega aquí otros campos según tus necesidades
            },
            required=['contenido']
        ),
        responses={
            200: 'Pregunta actualizada con éxito',
            400: 'Bad Request',
            404: 'No encontrado'
        }
    )
#api/preguntas/<int:id_pregunta>/ -> DELETE
def eliminarPregunta_swagger():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id_pregunta',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID de la pregunta a eliminar',
                required=True
            )
        ],
        responses={
            200: 'Pregunta eliminada con éxito',
            404: 'No encontrado'
        }
    )

############################################################
# Respuestas

def enviarRespuestas_swagger():
    return swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id_usuario',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID del usuario',
                required=True
            ),
            openapi.Parameter(
                name='id_evaluacion',
                in_=openapi.IN_PATH,
                type=openapi.TYPE_INTEGER,
                description='ID de la evaluación',
                required=True
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID de la pregunta'),
                    'respuesta': openapi.Schema(type=openapi.TYPE_STRING, description='Respuesta a la pregunta')
                },
                required=['id', 'respuesta']
            ),
            description='Datos de las respuestas'
        ),
        responses={
            201: 'Respuestas creadas exitosamente',
            400: 'Bad Request',
            # Agrega aquí otras respuestas según tus necesidades
        }
    )
############################################################