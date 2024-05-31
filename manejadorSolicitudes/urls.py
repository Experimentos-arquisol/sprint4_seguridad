from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.solicitud_view, name='solicitud_view'),
    path('registro/', views.enviar_solicitud, name='enviar_solicitud'),
    path('verSolicitud/', views.ver_solicitud, name='ver_solicitud'),
    path('verSolicitudes/', views.ver_solicitudes, name='ver_solicitudes')
    # path('esperar/', views.esperar, name='esperar'),
]