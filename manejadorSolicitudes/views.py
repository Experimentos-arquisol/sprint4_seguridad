from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse
from .logic import solicitudes_logic as sl
from django.http import QueryDict
from django.http import JsonResponse




@csrf_exempt
def solicitud_view(request): 

    if request.method == 'GET':
            return render(request, 'solicitud/index.html')



@csrf_exempt
def enviar_solicitud(request):
    if request.method == 'GET':
        return render(request, 'solicitud/registro.html')

    elif request.method == 'POST':
        data = request.POST
        # Procesar la solicitud con los datos modificados
        solicitud = sl.enviar_solicitud(data)
        
        try:
            url_crm = 'http://localhost:8000/validar_cliente/'
            response = requests.post(url_crm, data=data["correo"])
            response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
            return render(request, 'solicitud/creacion.html')
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error al enviar la solicitud al Banco: {e}", status=500)

@csrf_exempt
def ver_solicitud(request):
    if request.method == 'GET':
        return render(request, 'solicitud/consultar.html')

    elif request.method == 'POST':
        data = request.POST
        try:
            solicitud = sl.consultar_solicitud(data['correo'])
            return render(request, 'solicitud/solicitud_lista.html', {'solicitud': solicitud })
        except requests.exceptions.RequestException as e:
            return HttpResponse(f"Error al consultar la solicitud al Banco: {e}", status=500)

def ver_solicitudes(request):
    if request.method == 'GET':
        solicitudes = sl.consultar_solicitudes()
        return render(request, 'solicitud/vista_solicitudes.html', {'solicitudes': solicitudes})




@csrf_exempt
def esperar(request):
    return render(request, 'solicitud/espera.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)


