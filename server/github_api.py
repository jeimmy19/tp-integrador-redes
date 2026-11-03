
# Importamos requests para realizar solicitudes HTTP.
import requests


# Dirección base de la API REST de GitHub.
API_URL = "https://api.github.com"


def obtener_repositorios(username):
    """
    Consulta los repositorios públicos de un usuario de GitHub.
    """

    # Construimos la dirección de consulta.
    url = f"{API_URL}/users/{username}/repos"

    # Definimos los parámetros de la solicitud.
    parametros = {
        "per_page": 100,
        "sort": "updated"
    }

    try:
        # Realizamos la solicitud a GitHub.
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=15
        )

        # Comprobamos si la solicitud fue exitosa.
        respuesta.raise_for_status()

        # Convertimos la respuesta JSON en una lista de Python.
        repositorios = respuesta.json()

        # Devolvemos solamente los datos necesarios.
        return [
            {
                "nombre": repo["name"],
                "url": repo["html_url"]
            }
            for repo in repositorios
        ]

    except requests.RequestException as error:
        print(f"Error al consultar repositorios: {error}")
        return None


def obtener_followers(username):
    """
    Consulta los seguidores públicos de un usuario de GitHub.
    """

    # Construimos la dirección de consulta.
    url = f"{API_URL}/users/{username}/followers"

    # Definimos la cantidad máxima de resultados.
    parametros = {
        "per_page": 100
    }

    try:
        # Realizamos la solicitud a GitHub.
        respuesta = requests.get(
            url,
            params=parametros,
            timeout=15
        )

        # Comprobamos si la solicitud fue exitosa.
        respuesta.raise_for_status()

        # Convertimos la respuesta JSON en una lista de Python.
        followers = respuesta.json()

        # Devolvemos los datos necesarios de cada seguidor.
        return [
            {
                "nombre": follower["login"],
                "url": follower["html_url"]
            }
            for follower in followers
        ]

    except requests.RequestException as error:
        print(f"Error al consultar followers: {error}")
        return None
