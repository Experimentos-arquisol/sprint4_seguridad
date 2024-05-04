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
            correo_usuario = request.session.get('correo')
            if correo_usuario is None:
                return redirect('iniciar_sesion')  # Redirige si no hay sesión de usuario

            # Hacer una copia mutable del QueryDict
            data = request.POST.copy()
            data['correo'] = correo_usuario  # Agregar el correo al QueryDict mutable
            # print(data)

            # Procesar la solicitud con los datos modificados
            solicitud = sl.enviar_solicitud(data)
            # print('datpssss')
            # print(solicitud)
            # print('datpssss')

            url_manejador_ofertas = 'http://localhost:8000/ofertas/'

            try:
                response = requests.post(url_manejador_ofertas, json=solicitud)
                response.raise_for_status()
                oferta_info = response.json()
                return render(request, 'solicitud/solicitud_lista.html', {'oferta': oferta_info['oferta']})
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error al enviar la solicitud al Banco: {e}", status=500)

    @csrf_exempt
    def ver_solicitud(request):
        if request.method == 'GET':
            return render(request, 'solicitud/consultar.html')

        elif request.method == 'POST':
            data = request.POST


            url_manejador_ofertas = 'http://localhost:8000/ofertas/consultarOferta'

            try:
                response = requests.post(url_manejador_ofertas, data=data)
                print('llego')
                response.raise_for_status()
                oferta_info = response.json()
                # print(oferta_info)
                return render(request, 'solicitud/solicitud_lista.html', {'oferta': oferta_info})
            except requests.exceptions.RequestException as e:
                return HttpResponse(f"Error al consultar la solicitud al Banco: {e}", status=500)

            



@csrf_exempt
def esperar(request):
    return render(request, 'solicitud/espera.html')

def health_check(request):
    return JsonResponse({'message': 'OK'}, status=200)


