"""
URL configuration for SEL4C project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import UsuarioPerfilView

urlpatterns = [
    path('api/user/profile/<int:id>/', PerfilUsuarioView.as_view(), name='perfil-usuario'),
    path('api/user/login/', IniciarSesionView.as_view(), name='iniciar-sesion'),
    path('api/user/signup/', RegistroUsuarioView.as_view(), name='registro-usuario'),
]
