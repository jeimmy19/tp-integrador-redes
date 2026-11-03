# TP Integrador – Programación sobre Redes

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación cliente-servidor utilizando Python y sockets TCP.

La aplicación permitirá que varios clientes se conecten simultáneamente a un servidor, se autentiquen mediante usuario y contraseña y puedan intercambiar mensajes. También contará con comandos para consultar información de GitHub y administrar las conexiones activas.

El desarrollo se realizará de manera progresiva, incorporando y probando cada funcionalidad.

## Tecnologías utilizadas

- **Python:** lenguaje de programación.
- **Sockets TCP:** comunicación entre cliente y servidor.
- **Threading:** gestión de múltiples conexiones simultáneas.
- **SQLite:** almacenamiento de usuarios y datos consultados.
- **Visual Studio Code:** entorno de desarrollo.
- **Ubuntu WSL2:** entorno Linux de trabajo.
- **Git y GitHub:** control de versiones y publicación del proyecto.

## Estructura del proyecto

```text
tp-integrador-redes/
│
├── client/
│   └── cliente.py
│
├── server/
│   ├── autenticacion.py
│   ├── comandos.py
│   ├── github_api.py
│   └── servidor.py
│
├── database/
│   ├── conexion.py
│   └── inicializar_db.py
│
├── .venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## Avances realizados

### 1. Preparación del entorno de desarrollo

- Instalación y configuración de Ubuntu mediante WSL2.
- Preparación del proyecto en Visual Studio Code.
- Creación del directorio principal `tp-integrador-redes`.
- Instalación de Python y herramientas necesarias para trabajar con entornos virtuales.
- Creación del entorno virtual `.venv`.
- Activación y verificación del entorno virtual.

### 2. Verificación de herramientas

Se verificaron las versiones de las herramientas principales:

| Herramienta | Versión |
|---|---|
| Python | 3.14.4 |
| pip | 25.1.1 |
| SQLite | 3.46.1 |

### 3. Organización del proyecto

Se crearon las carpetas y archivos iniciales para separar las responsabilidades del sistema:

- `client`: contendrá el código del cliente.
- `server`: contendrá la lógica del servidor, autenticación y comandos.
- `database`: contendrá la conexión y las operaciones de la base de datos.

### 4. Base de datos

Se comenzó a preparar el módulo `inicializar_db.py`, destinado a crear la base de datos SQLite y sus tablas principales:

- `usuarios`
- `repositorios`
- `followers`

La implementación y verificación de estas tablas forman parte de la etapa actual de desarrollo.

## Funcionalidades previstas

El sistema deberá implementar:

1. Conexión de múltiples clientes mediante sockets TCP.
2. Autenticación de usuarios utilizando una base de datos.
3. Rechazo de credenciales incorrectas y cierre de la conexión.
4. Comunicación bidireccional entre clientes.
5. Interpretación de mensajes que comiencen con `/` como comandos.
6. Consulta y almacenamiento de repositorios de GitHub mediante `/repos usuario`.
7. Consulta y almacenamiento de seguidores de GitHub mediante `/followers usuario`.
8. Consulta de la hora del servidor mediante `/hora`.
9. Envío de mensajes a todos los clientes conectados mediante `/todos mensaje`.
10. Listado de usuarios conectados mediante `/usuarios`.
11. Desconexión del cliente mediante `/adios`.

## Requisitos e instalación

Se utilizará un entorno virtual para instalar y administrar las dependencias del proyecto.

Activar el entorno virtual:

```bash
source .venv/bin/activate
```

Las dependencias del proyecto se documentarán en `requirements.txt`.

## Estado del proyecto

**En desarrollo.**

Actualmente se completó la preparación del entorno de trabajo y la estructura inicial del proyecto. Se está trabajando en la configuración de la base de datos SQLite.

## Autoría

Proyecto académico correspondiente al trabajo práctico integrador de la asignatura **Programación sobre Redes**.