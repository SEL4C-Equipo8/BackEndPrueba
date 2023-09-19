from rest_framework import serializers
from .modelsPrueba import Usuario, Actividades, Modulos, EvidenciaModulos, Evaluaciones, ResultadoEvaluaciones, Estadisticas, ProgresoActividades, ProgresoUsuarios, Administrador


# ===== USUARIO =====
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'


# ===== ACTIVIDADES =====        
class ActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividades
        fields = '__all__'

# ===== MODULOS =====        
class ModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulos
        fields = '__all__'

# ===== EVALUACIONES =====
class EvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluaciones
        fields = '__all__'

# ===== RESULTADO EVALUACIONES =====
class ResultadoEvaluacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoEvaluaciones
        fields = '__all__'

# ===== EVIDENCIA MODULOS ===== 
class EvidenciaModulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvidenciaModulos
        fields = '__all__'

# ===== ESTADISTICAS =====
class EstadisticasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estadisticas
        fields = '__all__'

# ===== PROGRESO ACTIVIDADES =====
class ProgresoActividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoActividades
        fields = '__all__'

# ===== PROGRESO USUARIOS =====
class ProgresoUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgresoUsuarios
        fields = '__all__'

# ===== ADMINISTRADOR =====
class AdministradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = '__all__'

