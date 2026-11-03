
# Importamos sqlite3 para trabajar con bases de datos SQLite.
import sqlite3

# Definimos el nombre del archivo de nuestra base de datos.
DB_NAME = "database/tp_integrador.db"


def inicializar_db():
    """
    Crea la base de datos y sus tablas si todavía no existen.
    """

    # Establecemos la conexión con SQLite.
    conexion = sqlite3.connect(DB_NAME)

    # Creamos un cursor para ejecutar instrucciones SQL.
    cursor = conexion.cursor()

    # Creamos la tabla de usuarios.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    # Creamos la tabla de repositorios.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repositorios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            github_username TEXT NOT NULL,
            repo_name TEXT NOT NULL,
            repo_url TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES usuarios(id)
        )
    """)

    # Creamos la tabla de followers.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS followers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            github_username TEXT NOT NULL,
            follower_name TEXT NOT NULL,
            follower_url TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES usuarios(id)
        )

        
        
    """)

        # Evitar repositorios duplicados
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_repositorios_unicos
        ON repositorios (user_id, github_username, repo_name)
    """)

    # Evitar followers duplicados
    cursor.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_followers_unicos
        ON followers (user_id, github_username, follower_name)
    """)

    # Guardamos los cambios realizados.
    conexion.commit()

    # Cerramos la conexión con la base de datos.
    conexion.close()

    print("Base de datos inicializada correctamente.")


# Ejecutamos la función cuando se inicia este archivo.
if __name__ == "__main__":
    inicializar_db()
