
import socket
import threading
import json

from server.autenticacion import autenticar_usuario, obtener_usuario
from server.comandos import procesar_comando


# Configuración del servidor
HOST = "0.0.0.0"
PUERTO = 5000

# Diccionario de clientes conectados
clientes_conectados = {}

# Lock para proteger el acceso al diccionario compartido
lock_clientes = threading.Lock()


def enviar_mensaje(cliente_socket, mensaje):
    """Envía un mensaje de texto al cliente."""
    cliente_socket.sendall(mensaje.encode("utf-8"))


def atender_cliente(cliente_socket, direccion):
    """
    Atiende la comunicación con un cliente conectado.
    Recibe sus credenciales y mantiene la sesión activa.
    """

    print(f"Cliente conectado desde: {direccion}")

    username = None

    try:
        # Recibir las credenciales
        datos_recibidos = cliente_socket.recv(1024).decode("utf-8")

        credenciales = json.loads(datos_recibidos)

        username = credenciales["username"]
        password = credenciales["password"]

        # Validar las credenciales
        if not autenticar_usuario(username, password):

            respuesta = {
                "estado": "error",
                "mensaje": "Usuario o contraseña incorrectos."
            }

            enviar_mensaje(
                cliente_socket,
                json.dumps(respuesta)
            )

            print(f"Acceso rechazado para: {username}")
            return

        # Obtener los datos del usuario
        usuario = obtener_usuario(username)

        if usuario is None:
            enviar_mensaje(
                cliente_socket,
                json.dumps({
                    "estado": "error",
                    "mensaje": "No se encontraron los datos del usuario."
                })
            )
            return

        # Enviar bienvenida
        respuesta = {
            "estado": "ok",
            "mensaje": f"Bienvenido {username}"
        }

        enviar_mensaje(
            cliente_socket,
            json.dumps(respuesta)
        )

        print(f"Usuario autenticado: {username}")

        # Registrar al cliente conectado
        with lock_clientes:
            clientes_conectados[username] = {
                "socket": cliente_socket,
                "usuario": usuario
            }

        # Mantener la comunicación con el cliente
        while True:

            datos = cliente_socket.recv(1024)

            if not datos:
                break

            mensaje = datos.decode("utf-8").strip()

            if not mensaje:
                continue

            # Procesar comandos
            if mensaje.startswith("/"):

                resultado = procesar_comando(
                    mensaje,
                    usuario,
                    clientes_conectados
                )

                # Comando /todos
                if isinstance(resultado, dict) and resultado["tipo"] == "broadcast":

                    texto = resultado["mensaje"]

                    with lock_clientes:
                        destinatarios = [
                            datos_cliente["socket"]
                            for datos_cliente in clientes_conectados.values()
                        ]

                    for destinatario in destinatarios:
                        try:
                            enviar_mensaje(destinatario, texto)
                        except OSError:
                            pass

                # Comando /adios
                elif isinstance(resultado, dict) and resultado["tipo"] == "desconexion":

                    enviar_mensaje(
                        cliente_socket,
                        resultado["mensaje"]
                    )
                    break

                # Los demás comandos
                elif isinstance(resultado, str):

                    enviar_mensaje(cliente_socket, resultado)

            # Mensaje normal del chat
            else:

                texto = f"[{username}]: {mensaje}"

                with lock_clientes:
                    destinatarios = [
                        datos_cliente["socket"]
                        for datos_cliente in clientes_conectados.values()
                    ]

                for destinatario in destinatarios:
                    try:
                        enviar_mensaje(destinatario, texto)
                    except OSError:
                        pass

    except Exception as error:
        print(f"Error atendiendo al cliente {direccion}: {error}")

    finally:

        # Eliminar al usuario del registro al finalizar la sesión
        if username is not None:
            with lock_clientes:
                clientes_conectados.pop(username, None)

        cliente_socket.close()
        print(f"Conexión cerrada: {direccion}")


def iniciar_servidor():
    """
    Inicia el servidor TCP y acepta múltiples clientes.
    """

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    try:
        servidor.bind((HOST, PUERTO))
        servidor.listen()

        print(f"Servidor escuchando en {HOST}:{PUERTO}")
        print("Esperando conexiones de clientes...")

        while True:

            cliente_socket, direccion = servidor.accept()

            hilo = threading.Thread(
                target=atender_cliente,
                args=(cliente_socket, direccion)
            )

            hilo.start()

    except Exception as error:
        print(f"Error en el servidor: {error}")

    finally:
        servidor.close()


if __name__ == "__main__":
    iniciar_servidor()

