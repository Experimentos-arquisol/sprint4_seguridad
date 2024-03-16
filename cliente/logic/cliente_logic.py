import random
from ..models import Cliente

def get_clientes():
    clientes = Cliente.objects.all()
    return clientes

def create_cliente_from_form(form_data):
    try:
        nuevo_cliente = Cliente.objects.create(
            nombre=form_data['nombre'],
            apellido=form_data['apellido'],
            usuario=form_data['usuario'],
            correo=form_data['correo'],
            telefono=form_data['telefono'],
        )
        nuevo_cliente.save()

        cliente = {
            "nombre": form_data['nombre'],
            "apellido": form_data['apellido'],
            'usuario' : form_data['usuario'],
            'correo': form_data['correo'],
            'telefono': form_data['telefono'],
        }


        return cliente

        
    except Exception as e:
        return None


def generar_numero_aleatorio():
    # Genera un número aleatorio de 6 dígitos
    numero = random.randint(100000, 999999)
    return numero

def validar_numero(numero_ingresado, numero_almacenado):
    if int(numero_ingresado) == int(numero_almacenado):
        return True
    else:
        return False
