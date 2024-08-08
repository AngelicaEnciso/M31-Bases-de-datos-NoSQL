import requests
import pandas as pd

# URL de la API
url = "https://66b4e50e9f9169621ea4c25a.mockapi.io/api/v1/contactos"

# Realizar la solicitud GET a la API
response = requests.get(url)

# Comprobar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en formato JSON
    contactos_json = response.json()

    # Mostrar los datos en formato JSON formateado
    print("Datos en formato JSON formateado:")
    print(contactos_json)

    # Convertir los datos a un DataFrame de pandas
    df_contactos = pd.DataFrame(contactos_json)

    # Mostrar el DataFrame
    print("\nDatos en formato DataFrame:")
    print(df_contactos)

    # Exportar el DataFrame a un archivo CSV
    csv_filename = "contactos.csv"
    df_contactos.to_csv(csv_filename, index=False)

    print(f"\nDatos exportados a {csv_filename}")
else:
    print(f"Error al consultar la API: {response.status_code}")
