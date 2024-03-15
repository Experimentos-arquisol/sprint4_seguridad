from django.http import JsonResponse
from ..models import ApiBanco


def create_cliente(data):

    cliente = ApiBanco(nombre=data['nombre'], apellido=data['apellido'], usuario= data['usuario'] ,correo=data['correo'], telefono=data['telefono'])
    cliente.save()
    return JsonResponse({"mensaje": "Cliente creado exitosamente"}, status=201)


def buscar_cliente(correo_usuario):
    # Suponiendo que tienes un modelo Cliente con un campo 'correo'
    try:
        cliente = ApiBanco.objects.get(correo=correo_usuario)
        return {'existe': True, 'telefono': cliente.telefono}
    except ApiBanco.DoesNotExist:
        return None