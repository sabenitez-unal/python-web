import requests
import json
from requests.exceptions import HTTPError

def main():
    nombre_pokemon = input("Escribe el nombre del pokemon sobre el cual quieres consultar: ")

    nombre_pokemon.lower().strip()

    pokemonsReading(nombre_pokemon)

    with open(f"pokemon-{nombre_pokemon}.json") as pokemon:
        pokemonData = json.load(pokemon)

    if pokemonData:
        data = {
            "Nombre": pokemonData["name"],
            "ID": pokemonData["id"],
            "Tipo Principal": pokemonData["types"][0]["type"]["name"]
        }

        print("")
        for k, v in data.items():
            print(f"{k}: {str(v).capitalize()}")
        print("")

    else:
        print("No se pudo recuperar la información del pokemón. :(")

def pokemonsReading(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        with open(f"pokemon-{name}.json", "w") as pokemones:
            data = response.json()
            json.dump(data, pokemones, indent=4)

    except HTTPError as http_err:
        print(f"Ha sucedido un error HTTP: {http_err}")
        exit()
    except Exception as err:
        print(f"Ha sucedido un error: {err}")
        exit()

if __name__ == "__main__":
    main()