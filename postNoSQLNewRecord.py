#Angie Enciso
import requests

# URL de la API
url = "https://66b4e50e9f9169621ea4c25a.mockapi.io/api/v1/contactos"

# Datos del nuevo registro que deseas agregar
nuevo_registro = {
    "nombre": "Ana Gómez",
    "email": "ana.gomez@example.com",
    "telefono": "555-9876",
    "direccion": "Avenida Siempre Viva 742"
}

# Realizar la solicitud POST a la API para agregar el nuevo registro
response = requests.post(url, json=nuevo_registro)

# Comprobar si la solicitud fue exitosa
if response.status_code == 201:
    # Mostrar el registro agregado que devuelve la API
    registro_agregado = response.json()
    print("Nuevo registro agregado:")
    for key, value in registro_agregado.items():
        print(f"{key}: {value}")
else:
    print(f"Error al agregar el registro: {response.status_code}")
