from http.client import ResponseNotReady
import random
from django.shortcuts import render, redirect
from django.urls import reverse
from .logic import cliente_logic as cl
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseBadRequest
import requests
from django.conf import settings
import urllib.request
import urllib.parse
import os
from telesign.messaging import MessagingClient




@csrf_exempt
def clientes_view(request):
    if request.method == 'GET':
        return render(request, 'cliente/index.html')
    elif request.method == 'POST':
        url_api_validacion = 'http://localhost:8000/api/validar_cliente/'
        email = request.POST.get('correo')
    
        
        try:
            response = requests.post(url_api_validacion, data={'correo': email})
            response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        except:
            print("aaaaa")

        if response.json().get('existe', False):
            return redirect(validar_usuario)
        else:
            return render(request, 'cliente/registro2.html')

@csrf_exempt
def crear_usuario(request):
    data = request.POST
    cliente = cl.create_cliente_from_form(data)
    try:
        url_api_banco = 'http://localhost:8000/api/'
        response = requests.post(url_api_banco, data=cliente, json=cliente)
        response.raise_for_status()  # Lanza una excepción si la solicitud no es exitosa
        return render(request, 'cliente/index.html')
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"Error al registrar el cliente en el API de Banco: {e}")


@csrf_exempt
def validar_usuario(request):
    email = request.POST.get('correo')
    url_api_banco = 'http://localhost:8000/api/validar_cliente/'

    try:
        response = requests.post(url_api_banco, data={'correo': email})
        print(response)
        response.raise_for_status  # Lanza una excepción si la solicitud no es exitosa

        if response.json().get('existe', False):

            telefono = response.json().get('telefono')
            print(telefono)
            request.session['correo'] = email  # Guarda en la sesión
            request.session['telefono'] = telefono
            otp = enviar_otp_telefono(telefono)
            request.session['otp'] = otp
            return redirect(vista_ingreso_contrasena)
        else:
            # Si el usuario o correo no existe, mostrar mensaje de error
            print("f")
            return redirect(iniciar_sesion)
    except requests.exceptions.RequestException as e:
        #return render(request, 'login_step_one.html', {'error': f"Error al validar el usuario: {e}"})
        pass


    return render(request, 'clienteindex.html')


def vista_ingreso_contrasena(request):
    correo = request.session.get('correo')  
    telefono = request.session.get('telefono')
    otp = request.session.get('otp')
    print(telefono)
    if correo:
        context = {'correo': correo , 'telefono' : telefono, 'otp': otp}
        return render(request, 'cliente/ingresoContrasenia.html', context)
    else:

        return redirect(iniciar_sesion)
    
def procesar_login(request):
    if request.method == 'POST':
        contrasena = request.POST.get('contrasena')
        print(contrasena)
        otp = request.session.get('otp')
        print(otp)
        if verificar_otp(contrasena, otp):
            return redirect(inicio_sesion_exitoso)
        return redirect(iniciar_sesion)




def enviar_otp_telefono(telefono):
    customer_id = os.getenv('CUSTOMER_ID', '6A4502A7-AB77-4C43-B919-41CD57E29051')
    api_key = os.getenv('API_KEY', 'b6sr2uFHN88PUSFTdyj/UjcRbT4tddMRzC0mEoNz2PQB/2MR1HJifXyflttmrQQXxfijYXbszR5WD8J3D7b2jw==')

    
    phone_number = os.getenv('PHONE_NUMBER', '57'+telefono)

    otp = cl.generar_numero_aleatorio()

    message = f'Tu otp es {otp}'
    message_type = "OTP"

    messaging = MessagingClient(customer_id, api_key)

    response = messaging.message(phone_number, message, message_type)

   
    print(f"\nResponse:\n{response.body}\n")

    return otp

def verificar_otp(otp, almacenado):
    return cl.validar_numero(otp, almacenado)




def registro_cliente_view(request):
    if request.method == 'GET':
        return render(request, 'cliente/registro.html')
    
def inicio_sesion_exitoso(request):
    return render(request, 'cliente/inicio.html')

def iniciar_sesion(request):
    return render(request, 'cliente/iniciarSesion.html')
