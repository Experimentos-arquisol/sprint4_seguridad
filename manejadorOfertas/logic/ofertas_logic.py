from django.http import JsonResponse
from ..models import Oferta


def crear_mostrar_oferta(data):
    correo = data.get('correo')
    # print(correo)
    # print(data)
    tipo_oferta = motor_viabilidad(data)
    # print(tipo_oferta)

    oferta = Oferta(correo = correo,tipo_oferta = tipo_oferta)
    oferta.save()
    # print(oferta.tipo_oferta)
    # print(oferta.correo)
    return JsonResponse({
        "mensaje": "Oferta creada exitosamente",
        "oferta": {
            "tipo_oferta": oferta.tipo_oferta,
            "correo": oferta.correo
            # Incluye aquí otros campos que necesites mostrar
        }
    }, status=201)


def     buscar_oferta(correo_usuario):
    try:
        oferta = Oferta.objects.get(correo=correo_usuario)
        return {'existe': True, 'correo': oferta.correo, 'oferta': oferta.tipo_oferta}
    except Oferta.DoesNotExist:
        return None


def motor_viabilidad(data):

    profesion = data.get('profesion')
    actividad_economica = data.get('actividad')
    empresa = data.get('empresa')
    ingresos = int(data.get('ingresos'))
    egresos = int(data.get('deudas'))


    umbrales_tarjetas = {
        'Tarjeta Platino': 10000,
        'Tarjeta Oro': 5000,
        'Tarjeta Plata': 2000,
    }
    
    # Definimos la puntuación inicial del solicitante
    puntuacion = 0

    # Aumentamos la puntuación basada en los ingresos netos (ingresos menos egresos)
    ingresos_netos = ingresos - egresos
    if ingresos_netos > 8000:
        puntuacion += 40
    elif ingresos_netos > 4000:
        puntuacion += 30
    elif ingresos_netos > 2000:
        puntuacion += 20
    else:
        puntuacion += 10

    # Evaluamos la actividad económica, la empresa y la profesión
    # Puedes agregar puntuación extra basado en estos criterios
    # Por ejemplo, actividades económicas con menos riesgo podrían aumentar la puntuación
    # Igualmente, trabajar en una empresa grande o reconocida podría ser un plus
    
    # Para el ejemplo, solo agregaremos una lógica simple
    if actividad_economica in ['Tecnologia', 'Finanzas']:
        puntuacion += 10
    if empresa in ['Uniandes', 'Google']:
        puntuacion += 10
    if profesion in ['Ingeniero', 'Economista', 'Doctor']:
        puntuacion += 10

    # Determinamos la categoría de la tarjeta basándonos en la puntuación
    categoria_tarjeta = 'Tarjeta Estándar'  # Tarjeta por defecto si no cumple para otra
    for categoria, umbral in umbrales_tarjetas.items():
        if ingresos_netos >= umbral:
            categoria_tarjeta = categoria
            break  # Rompemos el bucle ya que encontramos la tarjeta adecuada

    return categoria_tarjeta




