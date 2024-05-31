from ..models import ManejadorSolicitudes

def enviar_solicitud(form_data):
    try:
        # solicitud = ManejadorSolicitudes.objects.create(
        #     correo=form_data['correo'],
        #     profesion=form_data['profesion'],
        #     actividad_economica=form_data['actividad'],
        #     empresa=form_data['empresa'],
        #     ingresos=form_data['ingresos'],
        #     deudas=form_data['deudas'],
        # )
        doc_ref = db.collection('solicitudes').document('user_id')
        doc_ref.set({
            'correo': f'{form_data["correo"]}',
            'profesion': f'{form_data["profesion"]}',
            'actividad_economica': f'{form_data["actividad"]}',
            'empresa': f'{form_data["empresa"]}',
            'ingresos': f'{form_data["ingresos"]}',
            'deudas': f'{form_data["deudas"]}',
        })

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
        solicitudes = db.collection('solicitudes').stream()
        print(db.collection('solicitudes').stream())
        documents = [{doc.id: doc.to_dict()} for doc in solicitudes]
        print(documents)
        return solicitudes
    except Exception as e:
        return None
    
def consultar_solicitud(correo):
    try:
        solicitud = ManejadorSolicitudes.objects.get(correo=correo)
        return solicitud
    except Exception as e:
        return None