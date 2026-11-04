
# Importamos hashlib para generar hashes seguros de contraseñas.
import hashlib

# Importamos secrets para generar valores aleatorios.
import secrets

# Importamos nuestra función de conexión a SQLite.
from database.conexion import obtener_conexion


def generar_hash(password, salt=None):
    """
    Genera un hash seguro para proteger una contraseña.
    """

    # Si no recibimos un salt, generamos uno aleatorio.
    if salt is None:
        salt = secrets.token_hex(16)

    # Convertimos la contraseña y el salt a bytes.
    password_bytes = password.encode("utf-8")
    salt_bytes = bytes.fromhex(salt)

    # Generamos el hash utilizando PBKDF2.
    hash_password = hashlib.pbkdf2_hmac(
        "sha256",
        password_bytes,
        salt_bytes,
        600000
    )

    # Devolvemos el salt y el hash.
    return salt, hash_password.hex()


def registrar_usuario(username, password):
    """
    Registra un usuario nuevo en la base de datos.
    """

    # Generamos el salt y el hash de la contraseña.
    salt, password_hash = generar_hash(password)

    # Guardamos ambos valores juntos para poder verificarlos.
    hash_completo = salt + ":" + password_hash

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO usuarios (username, password_hash)
            VALUES (?, ?)
            """,
            (username, hash_completo)
        )

        conexion.commit()
        return True

    except Exception:
        conexion.rollback()
        return False

    finally:
        conexion.close()


def autenticar_usuario(username, password):
    """
    Comprueba si el usuario y la contraseña son correctos.
    """

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT password_hash FROM usuarios WHERE username = ?",
        (username,)
    )

    resultado = cursor.fetchone()
    conexion.close()

    # Si el usuario no existe, rechazamos la autenticación.
    if resultado is None:
        return False

    # Separamos el salt del hash almacenado.
    salt, hash_guardado = resultado[0].split(":", 1)

    # Generamos nuevamente el hash de la contraseña ingresada.
    _, hash_ingresado = generar_hash(password, salt)

    # Comparamos ambos hashes de forma segura.
    return secrets.compare_digest(hash_guardado, hash_ingresado)

def obtener_usuario(username):
    """
    Busca un usuario en la base de datos por su nombre.

    Devuelve su ID y nombre de usuario.
    """
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "SELECT id, username FROM usuarios WHERE username = ?",
        (username,)
    )

    resultado = cursor.fetchone()
    conexion.close()

    if resultado is None:
        return None

    return {
        "id": resultado[0],
        "username": resultado[1]
    }