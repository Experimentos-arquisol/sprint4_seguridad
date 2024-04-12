import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .logic import ofertas_logic as ol
from django.shortcuts import render, redirect


@csrf_exempt
def crear_mostrar_oferta(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))  # Deserializa el JSON del cuerpo de la solicitud
            print('Datos recibidos:', data)
            return ol.crear_mostrar_oferta(data)
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON inválido")

        # Si la función ol.crear_mostrar_oferta(data) espera un diccionario, asegúrate de que esta línea esté manejando los datos correctamente.
        # Además, asegúrate de que esta función retorne una instancia de HttpResponse o JsonResponse.

    else:
        return HttpResponseBadRequest("Método no permitido")
    
@csrf_exempt
def buscar_oferta(request):
    if request.method == 'POST':
        correo_usuario = request.POST.get('correo')
        if not correo_usuario:
            return JsonResponse({"error": "Falta el correo o usuario en la solicitud"}, status=400)

        resultado = ol.buscar_oferta(correo_usuario)
        if resultado:
            
            return render(request, 'ofertas/mostrarOferta.html', {'oferta': resultado['oferta']})
        else:
            return JsonResponse({"existe": False}, status=404)
