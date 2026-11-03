
# Importamos nuestra función para conectarnos a SQLite.
from database.conexion import obtener_conexion


def guardar_repositorios(user_id, github_username, repositorios):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        for repo in repositorios:
            cursor.execute(
                """
                INSERT OR IGNORE INTO repositorios
                (user_id, github_username, repo_name, repo_url)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, github_username, repo["nombre"], repo["url"])
            )

        conexion.commit()
        return True

    except Exception as error:
        conexion.rollback()
        print(f"Error al guardar repositorios: {error}")
        return False

    finally:
        conexion.close()

def guardar_followers(user_id, github_username, followers):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    try:
        for follower in followers:
            cursor.execute(
                """
                INSERT OR IGNORE INTO followers
                (user_id, github_username, follower_name, follower_url)
                VALUES (?, ?, ?, ?)
                """,
                (user_id, github_username, follower["nombre"], follower["url"])
            )

        conexion.commit()
        return True

    except Exception as error:
        conexion.rollback()
        print(f"Error al guardar followers: {error}")
        return False

    finally:
        conexion.close()
