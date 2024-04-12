from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.crear_mostrar_oferta, name='crear_mostrar_oferta'),
    path('consultarOferta/', views.buscar_oferta, name='buscar_oferta'),

]
