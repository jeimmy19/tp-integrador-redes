
# Importamos sqlite3 para trabajar con SQLite.
import sqlite3
# Importamos Path para construir una ruta segura al archivo.
from pathlib import Path

# Obtenemos la ubicación de este archivo.
DIRECTORIO_ACTUAL = Path(__file__).resolve().parent

# Definimos la ubicación de nuestra base de datos.
DB_NAME = DIRECTORIO_ACTUAL / "tp_integrador.db"

def obtener_conexion():
    """
    Crea y devuelve una conexión con la base de datos SQLite.
    """

    # Establecemos la conexión con SQLite.
    conexion = sqlite3.connect(DB_NAME)

    # Activamos el control de claves foráneas.
    conexion.execute("PRAGMA foreign_keys = ON")

    # Devolvemos la conexión para utilizarla en otros módulos.
    return conexion