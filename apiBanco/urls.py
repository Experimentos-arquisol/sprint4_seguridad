from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crear_cliente, name='crea_cliente'),
    path('validar_cliente/', views.validar_cliente, name='validar_cliente'),
    
]
