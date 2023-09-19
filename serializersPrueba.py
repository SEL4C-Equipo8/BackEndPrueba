from rest_framework import serializers
from .modelsPrueba import Usuario, Actividad, Modulo, EvidenciaModulo, Evaluacion, ResultadoEvaluacion, Estadistica, ProgresoActividad, ProgresoUsuarios, Administrador


# ===== USUARIO =====

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id_usuario', 'username', 'email', 'grado_ac', 'institucion', 'genero', 'edad', 'pais')

class ActualizarPerfilSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    grado_ac = serializers.CharField(max_length=100)
    institucion = serializers.CharField(max_length=200)
    genero = serializers.CharField(max_length=20)
    edad = serializers.IntegerField()
    pais = serializers.ChoiceField(choices=PAISES)

class RegistroUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    gradoAcademico = serializers.CharField(max_length=100)
    institucion = serializers.CharField(max_length=200)
    genero = serializers.CharField(max_length=20)
    edad = serializers.IntegerField()
    pais = serializers.ChoiceField(choices=PAISES)



# ===== EVALUACIONES =====

class ResultadoEvaluacionSerializer(serializers.Serializer):
    def to_internal_value(self, data):
        # Validar que el JSON de entrada tenga al menos las claves requeridas
        required_keys = ['id_evaluacion', 'competencia1', 'competencia2', 'competencia3', 'competencia4', 'competencia5']
        for key in required_keys:
            if key not in data:
                raise serializers.ValidationError(f"El campo '{key}' es requerido.")
        return data

    def create(self, validated_data):
        # Crear un nuevo resultado de evaluación con los datos proporcionados
        return ResultadoEvaluacion.objects.create(**validated_data)
    


# ===== EVIDENCIAS MODULOS ===== 
class EvidenciaModuloSerializer(serializers.Serializer):
    idRespuesta = serializers.IntegerField()
    idModulo = serializers.IntegerField()
    texto_res = serializers.CharField(allow_blank=True, allow_null=True)
    archivo_res = serializers.FileField(required=False)



# ===== ACTIVIDADES =====
class ObtenerActividadSerializer(serializers.Serializer):
    model = Actividad
    fields = ('id_actividad', 'titulo', 'imagen', 'descripcion', 'usuario')
    



