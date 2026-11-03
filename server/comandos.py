
from datetime import datetime

from server.github_api import (
    obtener_repositorios,
    obtener_followers
)

from database.operaciones import (
    guardar_repositorios,
    guardar_followers
)


def procesar_comando(mensaje, usuario, clientes_conectados):
    """
    Procesa los comandos enviados por los clientes.

    Args:
        mensaje: Texto recibido del cliente.
        usuario: Diccionario con los datos del usuario autenticado.
        clientes_conectados: Diccionario de usuarios conectados.

    Returns:
        Una respuesta de texto o un diccionario con una acción del servidor.
    """

    partes = mensaje.strip().split()

    if not partes:
        return None

    comando = partes[0].lower()

    # Consultar y guardar repositorios de GitHub
    if comando == "/repos":

        if len(partes) < 2:
            return "Uso correcto: /repos usuario"

        github_username = partes[1]

        repositorios = obtener_repositorios(github_username)

        if repositorios is None:
            return "Error al consultar los repositorios de GitHub."

        if not guardar_repositorios(
            usuario["id"],
            github_username,
            repositorios
        ):
            return "Error al guardar los repositorios en la base de datos."

        return (
            f"Se guardaron los repositorios de {github_username} correctamente. "
            f"Total consultado: {len(repositorios)}"
        )

    # Consultar y guardar seguidores de GitHub
    elif comando == "/followers":

        if len(partes) < 2:
            return "Uso correcto: /followers usuario"

        github_username = partes[1]

        followers = obtener_followers(github_username)

        if followers is None:
            return "Error al consultar los followers de GitHub."

        if not guardar_followers(
            usuario["id"],
            github_username,
            followers
        ):
            return "Error al guardar los followers en la base de datos."

        return (
            f"Se guardaron los followers de {github_username} correctamente. "
            f"Total consultado: {len(followers)}"
        )

    # Consultar la hora del servidor
    elif comando == "/hora":

        hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return f"Hora del servidor: {hora_actual}"

    # Listar usuarios conectados
    elif comando == "/usuarios":

        usuarios = list(clientes_conectados.keys())

        if not usuarios:
            return "No hay usuarios conectados."

        return "Usuarios conectados: " + ", ".join(usuarios)

    # Enviar mensaje a todos los clientes
    elif comando == "/todos":

        if len(partes) < 2:
            return "Uso correcto: /todos mensaje"

        texto = " ".join(partes[1:])

        return {
            "tipo": "broadcast",
            "mensaje": f"[{usuario['username']}]: {texto}"
        }

    # Desconectar al usuario
    elif comando == "/adios":

        return {
            "tipo": "desconexion",
            "mensaje": f"¡Hasta luego, {usuario['username']}!"
        }

    # Comando desconocido
    else:

        return "Comando no reconocido."
