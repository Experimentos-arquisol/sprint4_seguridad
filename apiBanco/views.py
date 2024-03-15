from django.http import JsonResponse
from django.shortcuts import render, redirect
from .logic import api_logic as al
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def crear_cliente(request):
    if request.method == 'POST':
        data = request.POST # Los datos del cliente enviados desde cliente
        # Crea un nuevo cliente en la base de datos de apiBanco
        return al.create_cliente(data)

@csrf_exempt
def validar_cliente(request):
    if request.method == 'POST':
        correo_usuario = request.POST.get('correo')
        if not correo_usuario:
            return JsonResponse({"error": "Falta el correo o usuario en la solicitud"}, status=400)

        resultado = al.buscar_cliente(correo_usuario)
        if resultado:
            # Si 'buscar_cliente' encontró el cliente, 'resultado' contiene un diccionario con datos útiles.
            return JsonResponse({"existe": True, "telefono": resultado['telefono']}, status=200)
        else:
            # Si 'buscar_cliente' retorna None, el cliente no existe.
            return JsonResponse({"existe": False}, status=404)  # O considera usar 200 si prefieres no usar 404 para indicar ausencia
