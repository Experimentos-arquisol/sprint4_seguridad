from ..models import ManejadorSolicitudes

def enviar_solicitud(form_data):
    try:
        solicitud = ManejadorSolicitudes.objects.create(
            profesion=form_data['profesion'],
            actividad_economica=form_data['actividad'],
            empresa=form_data['empresa'],
            ingresos=form_data['ingresos'],
            deudas=form_data['deudas'],
        )
        solicitud.save()

        solicitud = {
            "profesion":form_data['profesion'],
            "actividad":form_data['actividad'],
            "empresa":form_data['empresa'],
            "ingresos":form_data['ingresos'],
            "deudas":form_data['deudas'],
            "correo":form_data['correo'],
        }


        return solicitud

        
    except Exception as e:
        return None