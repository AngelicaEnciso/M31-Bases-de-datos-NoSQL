import requests

# Base URL de la API
base_url = "https://66b4e50e9f9169621ea4c25a.mockapi.io/api/v1/contactos"

# ID del registro que deseas consultar (reemplaza '1' con el ID que desees)
registro_id = 10

# URL completa para consultar el registro específico
url = f"{base_url}/{registro_id}"

# Realizar la solicitud GET a la API para obtener el registro específico
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en formato JSON
    registro_json = response.json()

    # Mostrar todos los campos en formato plano
    print(f"Registro ID: {registro_id}")
    for key, value in registro_json.items():
        print(f"{key}: {value}")
else:
    print(f"Error al consultar la API: {response.status_code}")
