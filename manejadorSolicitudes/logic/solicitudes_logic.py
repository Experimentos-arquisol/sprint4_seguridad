from ..models import ManejadorSolicitudes

def enviar_solicitud(form_data):
    try:
        solicitud = ManejadorSolicitudes.objects.create(
            correo=form_data['correo'],
            profesion=form_data['profesion'],
            actividad_economica=form_data['actividad'],
            empresa=form_data['empresa'],
            ingresos=form_data['ingresos'],
            deudas=form_data['deudas'],
        )
        solicitud.save()

        # solicitud = {
        #     "profesion":form_data['profesion'],
        #     "actividad":form_data['actividad'],
        #     "empresa":form_data['empresa'],
        #     "ingresos":form_data['ingresos'],
        #     "deudas":form_data['deudas'],
        #     "correo":form_data['correo'],
        # }


        # return solicitud

        
    except Exception as e:
        return None
    
def consultar_solicitudes():
    try:
        solicitudes = ManejadorSolicitudes.objects.all()
        return solicitudes
    except Exception as e:
        return None
    
def consultar_solicitud(correo):
    try:
        solicitud = ManejadorSolicitudes.objects.get(correo=correo)
        return solicitud
    except Exception as e:
        return None