import requests
from requests.exceptions import HTTPError
import json

# Definición de la URL del endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Captura de excepciones en caso de algún error.
try:
    # Hago una solicitud GET al endpoint
    response = requests.get(url, timeout=10)  # Agrego un timeout de 10 segundos para evitar bloqueos prolongados
    response.raise_for_status() # Se obtiene el código de estado.
    
    # Guardado del archivo json del response en local.
    with open("posts.json", "w") as posts:
        data = response.json()
        json.dump(data, posts, indent=4)

except HTTPError as http_err:
    print(f"Ha ocurrido un error HTTP de código {http_err}")
except Exception as err:
    print(f"Ha ocurrido un error: {err}")