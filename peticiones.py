import requests
from concurrent.futures import ThreadPoolExecutor

# Define la función que envía una petición
def enviar_peticion():
    # Asegúrate de reemplazar esta línea con tu petición exportada de Insomnia
    response = requests.post("http://34.41.179.190:8000", json={"correo": "1correo@prueba"})
    print(response.status_code)

# Número de peticiones a enviar
numero_peticiones = 100

# Crea un ThreadPoolExecutor para enviar las peticiones en paralelo
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(enviar_peticion) for _ in range(numero_peticiones)]

# Espera a que todas las peticiones se completen
for future in futures:
    future.result()
