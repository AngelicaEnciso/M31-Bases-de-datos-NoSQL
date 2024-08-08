#Angie Enciso
import requests

# URL base de la API
base_url = "https://66b4e50e9f9169621ea4c25a.mockapi.io/api/v1/contactos"

# ID del registro que deseas modificar (reemplaza '1' con el ID del registro a modificar)
registro_id = 1

# URL completa para modificar el registro específico
url = f"{base_url}/{registro_id}"

# Datos actualizados del registro
datos_actualizados = {
    "nombre": "Ana Pérez",
    "email": "ana.perez@example.com",
    "telefono": "555-1234",
    "direccion": "Avenida Nuevo 456"
}

# Realizar la solicitud PUT a la API para actualizar el registro
response = requests.put(url, json=datos_actualizados)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Mostrar el registro actualizado que devuelve la API
    registro_actualizado = response.json()
    print("Registro actualizado:")
    for key, value in registro_actualizado.items():
        print(f"{key}: {value}")
else:
    print(f"Error al actualizar el registro: {response.status_code}")
