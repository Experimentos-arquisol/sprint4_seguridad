from django.contrib import admin
from django.urls import path, include
from . import views


appname = "api"
urlpatterns = [
    path('', views.clientes_view, name='clientes_view'),
    path('registro/', views.registro_cliente_view, name='registro_cliente'),
    path('inicio/', views.inicio_sesion_exitoso, name='inicio_sesion_exitoso'),
    path('iniciarSesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('validarUsuario/', views.validar_usuario, name='validar_usuario'),
    path('ingresoContrasenia/', views.vista_ingreso_contrasena, name='vista_ingreso_contrasena'),
    path('procesarLogin/', views.procesar_login, name='procesar_login')


    #path('api/', include('apiBanco.urls'))
]