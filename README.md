# TP Integrador – Programación sobre Redes

## Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación cliente-servidor utilizando Python y sockets TCP.

La aplicación permitirá que varios clientes se conecten simultáneamente a un servidor, se autentiquen mediante usuario y contraseña y puedan intercambiar mensajes.

También contará con comandos para consultar información de GitHub, almacenar los datos obtenidos en una base de datos SQLite y administrar las conexiones activas.

El desarrollo se realiza de manera progresiva, incorporando y probando cada funcionalidad.

## Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python 3.14.4 | Lenguaje de programación |
| Sockets TCP | Comunicación entre cliente y servidor |
| Threading | Gestión de múltiples conexiones simultáneas |
| SQLite 3.46.1 | Almacenamiento de usuarios y datos consultados |
| Requests | Consultas a la API de GitHub |
| JSON | Intercambio de información entre cliente y servidor |
| Visual Studio Code | Entorno de desarrollo |
| Ubuntu WSL2 | Entorno Linux de trabajo |
| Git y GitHub | Control de versiones y publicación |

## Estructura del proyecto

```text
tp-integrador-redes/
│
├── client/
│   ├── __init__.py
│   └── cliente.py
│
├── server/
│   ├── __init__.py
│   ├── autenticacion.py
│   ├── comandos.py
│   ├── github_api.py
│   └── servidor.py
│
├── database/
│   ├── __init__.py
│   ├── conexion.py
│   ├── inicializar_db.py
│   └── operaciones.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

> El entorno virtual `.venv` y la base de datos generada no se publican en GitHub.

## Avances realizados

### 1. Preparación del entorno de desarrollo

- Instalación y configuración de Ubuntu mediante WSL2.
- Preparación del proyecto en Visual Studio Code.
- Creación del directorio principal `tp-integrador-redes`.
- Instalación y configuración de Python.
- Creación del entorno virtual `.venv`.
- Activación y verificación del entorno virtual.

### 2. Verificación de herramientas

Se verificaron las siguientes versiones:

| Herramienta | Versión |
|---|---|
| Python | 3.14.4 |
| pip | 25.1.1 |
| SQLite | 3.46.1 |

### 3. Organización del proyecto

Se organizaron los módulos para separar las responsabilidades:

- `client`: comunicación y funcionalidades del cliente.
- `server`: servidor, autenticación, comandos e integración con GitHub.
- `database`: conexión, inicialización y operaciones de SQLite.

Se incorporaron archivos `__init__.py` para organizar los paquetes de Python y facilitar las importaciones entre módulos.

### 4. Base de datos SQLite

Se desarrolló el módulo de inicialización de la base de datos.

Se crearon las siguientes tablas:

- `usuarios`: almacenamiento de credenciales de los usuarios.
- `repositorios`: almacenamiento de repositorios consultados en GitHub.
- `followers`: almacenamiento de seguidores consultados en GitHub.

También se implementaron:

- Conexión a SQLite.
- Activación de claves foráneas.
- Relaciones entre usuarios y datos almacenados.
- Índices únicos para evitar registros duplicados.

Se verificó la inicialización y conexión a la base de datos.

### 5. Sistema de autenticación

Se desarrolló el módulo `autenticacion.py`, que permite:

- Registrar usuarios.
- Generar hashes de contraseñas utilizando PBKDF2 con SHA-256.
- Utilizar salt aleatorio para proteger las contraseñas.
- Validar las credenciales contra SQLite.
- Recuperar el identificador y nombre del usuario autenticado.

Se realizaron pruebas de autenticación con credenciales correctas e incorrectas.

### 6. Integración con GitHub API

Se desarrolló el módulo `github_api.py` utilizando la biblioteca Requests.

Se implementaron funciones para:

- Consultar los repositorios públicos de un usuario de GitHub.
- Consultar sus seguidores.
- Obtener nombres y enlaces de los resultados.
- Manejar errores de conexión y respuestas de la API.

Se realizaron consultas de prueba con un usuario real de GitHub.

### 7. Operaciones de almacenamiento

En `database/operaciones.py` se implementaron funciones para:

- Guardar repositorios consultados.
- Guardar seguidores consultados.
- Relacionar los registros con el usuario autenticado.
- Evitar duplicaciones mediante `INSERT OR IGNORE`.

Se verificó que los registros se almacenen correctamente y que las consultas repetidas no generen duplicados.

### 8. Procesamiento de comandos

En `server/comandos.py` se desarrolló la función `procesar_comando()` para interpretar los comandos enviados por los clientes.

| Comando | Funcionalidad |
|---|---|
| `/repos usuario` | Consulta y almacena repositorios de GitHub |
| `/followers usuario` | Consulta y almacena seguidores de GitHub |
| `/hora` | Devuelve la fecha y hora del servidor |
| `/todos mensaje` | Prepara un mensaje para todos los clientes |
| `/usuarios` | Lista los usuarios conectados |
| `/adios` | Prepara la despedida y desconexión |

Se realizaron pruebas individuales de procesamiento de comandos.

### 9. Servidor TCP

Se desarrolló el módulo `servidor.py` utilizando sockets TCP y threading.

Actualmente contempla:

- Creación del socket del servidor.
- Asociación a la dirección y puerto de escucha.
- Aceptación de conexiones entrantes.
- Creación de un hilo independiente para atender cada cliente.
- Recepción y validación de credenciales.
- Registro de usuarios autenticados.
- Procesamiento de mensajes y comandos.
- Preparación de la difusión de mensajes.
- Eliminación de usuarios al finalizar la sesión.

Se verificó el inicio del servidor y la escucha en el puerto 5000.

### 10. Cliente TCP

Se desarrolló el módulo `cliente.py` para establecer la conexión con el servidor.

Actualmente contempla:

- Conexión mediante sockets TCP.
- Envío de credenciales en formato JSON.
- Recepción de la respuesta de autenticación.
- Creación de un hilo para recibir mensajes del servidor.
- Envío de mensajes y comandos desde el teclado.
- Solicitud de desconexión mediante `/adios`.

Se verificó satisfactoriamente la conexión y autenticación de un usuario registrado.

## Funcionalidades previstas y estado de desarrollo

| Funcionalidad | Estado |
|---|---|
| Preparación del entorno | Completado |
| Creación de la base de datos | Completado |
| Autenticación de usuarios | Implementado y probado |
| Consulta de repositorios GitHub | Implementado y probado |
| Consulta de followers GitHub | Implementado y probado |
| Almacenamiento en SQLite | Implementado y probado |
| Procesamiento de comandos | Implementado y probado individualmente |
| Servidor TCP concurrente | Implementado, pendiente de pruebas integrales |
| Cliente TCP | Implementado, pendiente de pruebas integrales |
| Chat bidireccional | En desarrollo |
| Difusión de mensajes a todos los clientes | En desarrollo y pendiente de pruebas |
| Desconexión controlada | Pendiente de pruebas integrales |

## Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/jeimmy19/tp-integrador-redes.git
```

Ingresar al directorio:

```bash
cd tp-integrador-redes
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 5. Inicializar la base de datos

```bash
python -m database.inicializar_db
```

### 6. Iniciar el servidor

Desde la raíz del proyecto:

```bash
python -m server.servidor
```

El servidor quedará escuchando en el puerto 5000.

### 7. Ejecutar el cliente

Abrir otra terminal, activar el entorno virtual y ejecutar:

```bash
python -m client.cliente
```

El cliente solicitará las credenciales de un usuario previamente registrado en la base de datos.

## Estado actual del proyecto

**En desarrollo.**

Se completaron la preparación del entorno, la organización de los módulos, la implementación de SQLite, el sistema de autenticación, la integración con GitHub API y el procesamiento individual de comandos.

También se implementaron las primeras versiones del servidor TCP y del cliente, incluyendo la autenticación y la estructura de comunicación mediante hilos.

Actualmente se trabaja en completar y verificar la comunicación bidireccional, el intercambio de mensajes entre múltiples clientes y la ejecución integral de todos los comandos.

## Autoría

Proyecto académico correspondiente al trabajo práctico integrador de la asignatura **Programación sobre Redes**.

**Repositorio:** [github.com/jeimmy19/tp-integrador-redes](https://github.com/jeimmy19/tp-integrador-redes)