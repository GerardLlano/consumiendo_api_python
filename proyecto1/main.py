
import requests
import json


PATH_API = 'https://pokeapi.co/api/v2/pokemon/pikachu'


def llamada():
    try:
        global PATH_API
        url = PATH_API
        response = requests.get(url)
        response = json.loads(response.text)
        print(response)
    except FileExistsError:
        print("hubo un error")


if __name__ == "__main__":
    llamada()


"""
Esta es la documentación del proyecto:

1-Cree el archivo .gitignore
1-Realice un entorno virtual: python3 -m install venv venv
2-Active el entorno virtual: source venv/bin/activate
3-Cree un folder llamado [proyecto1 con el archivo main.py dentro de él]
  dentro de la carpeta venv
  -instalé requests: pip install requests
  -instalé flake8: pip install flake8

"""
