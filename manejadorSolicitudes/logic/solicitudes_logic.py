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
        solicitud = ManejadorSolicitudes.objects.get(correo=correo)
        return solicitud
    except Exception as e:
        return None