
# Importamos datetime para consultar la fecha y hora del servidor.
from datetime import datetime


def procesar_comando(mensaje, usuario, clientes_conectados):
    """
    Recibe un mensaje y determina qué comando debe ejecutar.
    
    mensaje: texto enviado por el cliente.
    usuario: nombre del usuario que envía el mensaje.
    clientes_conectados: diccionario de clientes conectados.
    """

    # Separamos el mensaje en palabras.
    partes = mensaje.strip().split()

    # Si el mensaje está vacío, no hacemos nada.
    if not partes:
        return None

    # Obtenemos el comando.
    comando = partes[0].lower()

    # Comando /hora.
    if comando == "/hora":
        hora_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"Hora del servidor: {hora_actual}"

    # Comando /usuarios.
    elif comando == "/usuarios":
        usuarios = list(clientes_conectados.keys())

        if not usuarios:
            return "No hay usuarios conectados."

        return "Usuarios conectados: " + ", ".join(usuarios)

    # Comando /todos.
    elif comando == "/todos":
        # Verificamos que exista un mensaje después del comando.
        if len(partes) < 2:
            return "Uso correcto: /todos mensaje"

        # Recuperamos el mensaje completo.
        texto = " ".join(partes[1:])

        # Devolvemos el mensaje para que el servidor lo distribuya.
        return {
            "tipo": "broadcast",
            "mensaje": f"[{usuario}]: {texto}"
        }

    # Comando /adios.
    elif comando == "/adios":
        return {
            "tipo": "desconexion",
            "mensaje": f"¡Hasta luego, {usuario}!"
        }

    # Comando desconocido.
    else:
        return "Comando no reconocido."
