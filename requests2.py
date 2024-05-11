import requests
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import datetime
import time


peticiones = []

tiempo_inicial = time.time()

def enviar_peticion(n):
    # Enviar la petición
    headers = {"api-key": "badUser344"}
    response = requests.post("http://34.30.171.140:8000", json={"correo": "1correo@prueba"}, headers=headers)
    # response = requests.post("http://35.188.104.109:8080/cliente/registro/", json={"correo": "1correo@prueba"}, headers=headers)

    momento = time.time() - tiempo_inicial

    peticiones.append({
        "Numero de Peticion": n,
        "Estado": response.status_code,
        "Headers": headers["api-key"],
        "Momento (s)": round(momento, 2)
    })
    
    print(f"{response.status_code} Petición {n}")

def main():
    numero_peticiones = 500

    global tiempo_inicial
    tiempo_inicial = time.time() 

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(enviar_peticion, i) for i in range(numero_peticiones)]

    for future in futures:
        future.result()

    df = pd.DataFrame(peticiones)

    cantidad_malas = len(df[df['Estado'] == 429])
    
    print(f'Peticiones rechazadas: {cantidad_malas}')
    print(f'# de peticiones: {numero_peticiones}')
    
    df.to_excel("resultados_peticiones.xlsx", index=False)

main()
