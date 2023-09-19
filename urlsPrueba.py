from django.urls import path
from .viewsPrueba import UsuarioPerfilView

urlpatterns = [
    path('api/user/profile/<int:id>/', PerfilUsuarioView.as_view(), name='perfil-usuario'),
    path('api/user/login/', IniciarSesionView.as_view(), name='iniciar-sesion'),
    path('api/user/signup/', RegistroUsuarioView.as_view(), name='registro-usuario'),
]