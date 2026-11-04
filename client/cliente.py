import socket
import json
import threading

HOST = "127.0.0.1"
PUERTO = 5000

def recibir_mensajes(cliente):
    """
    Escucha continuamente los mensajes enviados por el servidor.
    """

    while True:
        try:
            datos = cliente.recv(1024)

            if not datos:
                print("\nEl servidor cerró la conexión.")
                break

            mensaje = datos.decode("utf-8")
            print(f"\n{mensaje}")

        except OSError:
            break



def conectar_servidor():
    """
    Conecta el cliente con el servidor, valida las credenciales
    y permite intercambiar mensajes.
    """

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((HOST, PUERTO))

        username = input("Usuario: ")
        password = input("Contraseña: ")

        credenciales = {
            "username": username,
            "password": password
        }

        mensaje = json.dumps(credenciales)

        cliente.sendall(mensaje.encode("utf-8"))

        # Recibir la respuesta de autenticación
        respuesta = cliente.recv(1024).decode("utf-8")

        datos = json.loads(respuesta)

        print(datos["mensaje"])

        # Si las credenciales son incorrectas, finalizar
        if datos["estado"] != "ok":
            return

        # Crear hilo para recibir mensajes del servidor
        hilo_receptor = threading.Thread(
            target=recibir_mensajes,
            args=(cliente,),
            daemon=True
        )

        hilo_receptor.start()

        print("\nChat iniciado.")
        print("Escribe /adios para desconectarte.\n")

        # Enviar mensajes al servidor
        while True:

            texto = input()

            if not texto.strip():
                continue

            cliente.sendall(texto.encode("utf-8"))

            if texto.strip().lower() == "/adios":
                break

    except ConnectionRefusedError:
        print("No se pudo conectar con el servidor.")

    except Exception as error:
        print(f"Error de conexión: {error}")

    finally:
        cliente.close()
        print("Cliente desconectado.")



if __name__ == "__main__":
    conectar_servidor()
