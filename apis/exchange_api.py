import requests
import os
import json
from dotenv import load_dotenv

URL_API = "http://data.fixer.io/api/"
MODES = ["latest", "symbols"]

def main():
    # se selecciona el modo del programa.
    mode = select_mode()

    # se une el modo al endpoint de la API
    url = URL_API + mode

    if mode == MODES[0]:    # Modo latest
        base = input("Escriba el código de la moneda de la que quiere consultar la tasa de cambio: ").upper()
        symbols = input("Escriba el código de la moneda destino: ").upper()

        # Se obtiene la respuesta decodificada en JSON
        response = latest(url=url, base=base, symbols=symbols)
        data = decoding(response=response)

        print(data)

    elif mode == MODES[1]:  # Modo symbols

        response = api_request(url=url)
        data = decoding(response=response)

        divisas = data["symbols"]

        print("Se muestran los códigos de cada divisa: ")

        for key, value in divisas.items():
            print(f"{key} : {value}")


    else:                   # Modo convert
        # Pedir al usuario los datos necesarios.
        base = input("Escriba el código de la moneda desde la cual quiere convertir: ").upper()
        target = input("Escriba el código de la moneda a la cual va a convertir: ").upper()
        amount = int(input("Indique la cantidad a convetir: "))

        # Realizar la solicitud de conversión con ayuda de la función convert() y decodificación del JSON en diccionario.
        response = latest(url=url, base=base, symbols=target)
        data = decoding(response)
        
        result = amount * data["rates"][base]

        print(f"""  
            Para la fecha {data["date"]}, {amount} {data["base"]} equivalen a:
                - {result} {data["rates"].keys()}.
        """)


def api_request(url: str, params: dict = dict()):
    """
    Realiza una solicitud HTTP GET a la URL especificada con parámetros adicionales.
    
    Esta función carga la clave de API desde las variables de entorno y la añade 
    automáticamente a los parámetros de la solicitud. Maneja errores HTTP y otras 
    excepciones, terminando la ejecución del programa en caso de que ocurran.
    
    Args:
        url (str): La URL a la que se realizará la solicitud GET.
        params (dict, optional): Diccionario de parámetros a enviar en la solicitud.
                                 Por defecto es un diccionario vacío.
    
    Returns:
        requests.Response: El objeto de respuesta de la solicitud HTTP si es exitosa.
    
    Raises:
        requests.HTTPError: Si se recibe un error HTTP. Imprime el error y termina el programa.
        Exception: Si ocurre cualquier otro tipo de error. Imprime el error y termina el programa.
    
    Note:
        - Requiere que la variable de entorno 'EXCHANGE_RATE_API_KEY' esté configurada.
        - El programa se interrumpe (exit()) si hay cualquier error en la solicitud.
    """

    # Se cargan las variables de entorno con la api_key
    load_dotenv()
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")
    params["access_key"] = api_key

    try: 
        # Se obtiene respuesta a la petición.
        response = requests.get(url=url, params=params)
        response.raise_for_status()

        # Se retorna la respuesta como objeto requests.Response.
        return response
    # En caso de recibir un error HTTP
    except requests.HTTPError as http_e:
        print(f"Error HTTP: {http_e}")
        exit()
    # En caso de recibir otro tipo de error.
    except Exception as e:
        print(f"Error desconocido: {e}")
        exit()


def decoding(response: requests.Response):
    """
    Decodifica una respuesta HTTP y la guarda en un archivo JSON local.
    
    Esta función toma una respuesta de requests, la convierte a formato JSON,
    la almacena en un archivo llamado 'exchange_data.json' y retorna los datos
    decodificados como un diccionario.
    
    Args:
        response (requests.Response): Objeto de respuesta HTTP de la librería requests
                                      que contiene datos en formato JSON.
    
    Returns:
        dict: Diccionario con los datos decodificados del archivo JSON.
    
    Raises:
        SystemExit: Si ocurre un error durante la decodificación del archivo,
                    se imprime un mensaje de error y se termina la ejecución.
    
    Example:
        >>> response = requests.get('https://api.example.com/data')
        >>> data = decoding(response)
        >>> print(data)
    """

    try: 
        # Se decodifica la respuesta como archivo JSON y se guarda en local
        with open("apis/exchange_data.json", "w+") as data:
            json.dump(response.json(), data, indent=4)
            
        with open("apis/exchange_data.json", "r") as data:
            result = json.load(data)

        # Se retorna el diccionario con los datos JSON
        return result
    except Exception as e:
        print(f"Error decodificando el archivo: {e}")
        exit()

def select_mode():
    """
    Muestra un menú de opciones al usuario y solicita la selección de una operación.
    
    El menú presenta tres opciones disponibles:
    2. Saber qué símbolo tiene una moneda específica.
    3. Realizar la conversión de una cantidad de una moneda a otra.
    
    La función valida continuamente la entrada del usuario hasta que ingrese
    un número válido entre 1 y 3.
    
    Returns:
        str: El nombre de la opción seleccionada del diccionario MODES,
             correspondiente a la selección numérica del usuario (1, 2 o 3).
    
    Raises:
        ValueError: Si el usuario ingresa un valor que no puede convertirse a entero.
    """

    print("""
        ¿Qué quieres hacer?
          1. Consultar la última tasa de cambio del Euro.
          2. Saber qué código tiene mi moneda.
          3. Realizar la conversión de una cantidad específica de una moneda a otra.

        Es necesario conocer el código de las divisas a convertir.
    """)

    while True:
        # Usuario da la opcion de preferencia
        mode = int(input("Por favor, escriba el número de la opción de su preferencia: "))

        if 1 <= mode <= 3:
            if mode == 3: return MODES[0]
            return MODES[mode - 1] # Se retorna el nombre de la opción.
        else:
            print("Escriba una opción válida\n") # Se hace repetir la selección.

def latest(url: str, base: str, symbols: str):
    """
    Obtiene los tipos de cambio más recientes para una moneda base especificada.
    Parameters:
    -----------
    url : str
        La URL del endpoint de la API de tipos de cambio.
    base : str
        El código de la moneda base (ej: 'USD', 'EUR') para la cual se desean
        obtener los tipos de cambio.
    Returns:
    --------
    dict
        Un diccionario con los tipos de cambio más recientes de la moneda base
        especificada respecto a otras monedas.
    Raises:
    -------
    RequestException
        Si ocurre un error en la solicitud HTTP a la API.
    """

    params = {
        "base": base,
        "symbols": symbols
    }

    return api_request(url=url, params=params)

if __name__ == "__main__":
    print("Bienvenido al programa de conversión de moneda.")
    main()