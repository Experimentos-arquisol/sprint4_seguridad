from ..models import ManejadorSolicitudes
from django.conf import settings
from google.cloud import datastore

def enviar_solicitud(form_data):
    try:
        # Crea una entidad
        key = settings.DB.key('Solicitud')
        solicitud = datastore.Entity(key=key)
        solicitud.update({
            'correo': form_data['correo'],
            'profesion': form_data['profesion'],
            'actividad_economica': form_data['actividad'],
            'empresa': form_data['empresa'],
            'ingresos': form_data['ingresos'],
            'deudas': form_data['deudas'],
        })
        settings.DB.put(solicitud)
        return 'Solicitud guardada con éxito'
    except Exception as e:
        print(e)
        return str(e)
    
def consultar_solicitudes():
    try:
        query = settings.DB.query(kind='Solicitud')
        resultados = list(query.fetch())
        return [dict(result) for result in resultados]
    except Exception as e:
        print(e)
        return str(e)


def consultar_solicitud(correo):
    try:
        # Crear una consulta en Datastore para la entidad 'Solicitud'
        query = settings.DB.query(kind='Solicitud')
        query.add_filter('correo', '=', correo)
        resultado = list(query.fetch(limit=1))
        print(resultado)
        if resultado:
            # Devuelve el primer resultado como un diccionario
            return dict(resultado[0])
        else:
            # No se encontró ninguna solicitud con ese correo
            return None
    except Exception as e:
        print(e)
        return None