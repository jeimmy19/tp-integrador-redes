# TP Integrador – Programación sobre Redes

## Sistema de comunicación Cliente-Servidor con Python y Sockets TCP

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de una aplicación de comunicación cliente-servidor utilizando **Python y sockets TCP**, como trabajo integrador de la materia Programación sobre Redes.

El sistema permite establecer conexiones simultáneas entre varios clientes y un servidor, validar usuarios mediante una base de datos SQLite y mantener una comunicación bidireccional mediante mensajes de texto.

Además, incorpora comandos que permiten consultar información, interactuar con la API de GitHub y enviar mensajes a todos los clientes conectados.

## 2. Tecnologías utilizadas

- **Python 3.14.4:** lenguaje de programación.
- **Sockets TCP:** comunicación entre clientes y servidor.
- **Threading:** gestión de múltiples conexiones simultáneas.
- **SQLite:** almacenamiento de usuarios, repositorios y seguidores.
- **Requests:** realización de solicitudes HTTP a la API de GitHub.
- **JSON:** intercambio de información entre cliente y servidor.
- **Hashlib y Secrets:** protección de contraseñas mediante generación de hashes y sales.
- **Git y GitHub:** control de versiones y alojamiento del proyecto.
- **Ubuntu WSL2:** entorno de desarrollo.

## 3. Estructura del proyecto

```text
tp-integrador-redes/
│
├── client/
│   └── cliente.py
│
├── database/
│   ├── conexion.py
│   ├── inicializar_db.py
│   ├── operaciones.py
│   └── tp_integrador.db
│
├── server/
│   ├── autenticacion.py
│   ├── comandos.py
│   ├── github_api.py
│   └── servidor.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Descripción de los archivos

**Carpeta `client/`**

- `cliente.py`: establece la conexión con el servidor, envía las credenciales, recibe mensajes y permite al usuario interactuar mediante comandos.

**Carpeta `server/`**

- `servidor.py`: inicia el servidor TCP, acepta conexiones y gestiona múltiples clientes mediante hilos.
- `autenticacion.py`: realiza la validación de las credenciales de los usuarios.
- `comandos.py`: procesa los comandos enviados por los clientes.
- `github_api.py`: consulta la API de GitHub para obtener repositorios y seguidores.

**Carpeta `database/`**

- `conexion.py`: administra la conexión con la base de datos SQLite.
- `inicializar_db.py`: crea las tablas necesarias para el funcionamiento del sistema.
- `operaciones.py`: contiene las operaciones para almacenar y consultar información.
- `tp_integrador.db`: base de datos del proyecto.

## 4. Funcionalidades implementadas

### 4.1. Comunicación mediante sockets TCP

Se implementó una arquitectura cliente-servidor utilizando sockets TCP.

El servidor escucha conexiones en el puerto `5000` y permite que varios clientes se conecten simultáneamente.

### 4.2. Concurrencia

Se utiliza el módulo `threading` para atender a cada cliente en un hilo independiente.

Esto permite mantener varias conexiones activas sin bloquear la comunicación de los demás usuarios.

### 4.3. Autenticación de usuarios

Al conectarse, el cliente envía su nombre de usuario y contraseña.

El servidor valida las credenciales utilizando la información almacenada en SQLite.

Las contraseñas se procesan mediante PBKDF2-HMAC con SHA-256, utilizando sales y comparación segura.

Si las credenciales son incorrectas, el servidor rechaza la conexión y finaliza la sesión.

Si son correctas, el cliente recibe un mensaje de bienvenida.

**Importante:** para iniciar sesión, el usuario debe estar previamente registrado en la base de datos.

### 4.4. Comunicación bidireccional

Una vez autenticado, el cliente puede enviar mensajes al servidor y recibir respuestas.

También se implementó la recepción de mensajes mediante un hilo independiente en el cliente.

### 4.5. Comandos disponibles

El sistema reconoce los siguientes comandos:

| Comando | Descripción |
|---|---|
| `/repos usuario` | Consulta los repositorios públicos de un usuario de GitHub y los almacena en la tabla `repositorios`. |
| `/followers usuario` | Consulta los seguidores de un usuario de GitHub y los almacena en la tabla `followers`. |
| `/hora` | Devuelve la fecha y hora actual del servidor. |
| `/todos mensaje` | Envía un mensaje a todos los clientes conectados. |
| `/usuarios` | Muestra la lista de usuarios conectados. |
| `/adios` | Envía un mensaje de despedida y finaliza la conexión del cliente. |

### 4.6. Integración con GitHub

Se utiliza la biblioteca `requests` para realizar consultas a la API pública de GitHub.

La información obtenida se almacena en la base de datos SQLite.

Se implementaron las siguientes operaciones:

- Obtener repositorios de un usuario.
- Obtener seguidores de un usuario.
- Guardar los resultados en las tablas correspondientes.
- Evitar registros duplicados mediante restricciones de unicidad.

## 5. Base de datos

El proyecto utiliza SQLite para almacenar la información.

Se crearon las siguientes tablas:

| Tabla | Función |
|---|---|
| `usuarios` | Almacena los usuarios y sus datos de autenticación. |
| `repositorios` | Almacena los repositorios obtenidos desde GitHub. |
| `followers` | Almacena los seguidores obtenidos desde GitHub. |

La base de datos se encuentra en:

```text
database/tp_integrador.db
```

## 6. Instalación y configuración

### 6.1. Clonar el repositorio

```bash
git clone https://github.com/jeimmy19/tp-integrador-redes.git
```

Ingresar a la carpeta:

```bash
cd tp-integrador-redes
```

### 6.2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 6.3. Activar el entorno virtual

En Ubuntu o WSL2:

```bash
source .venv/bin/activate
```

### 6.4. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 6.5. Inicializar la base de datos

Desde la carpeta raíz del proyecto:

```bash
python -m database.inicializar_db
```

Este comando crea las tablas necesarias para el funcionamiento del sistema.

**Nota:** antes de iniciar el cliente, debe existir al menos un usuario registrado en la tabla `usuarios`.

## 7. Ejecución del sistema

Para probar la comunicación se deben utilizar varias terminales.

### Terminal 1: iniciar el servidor

Activar el entorno virtual y ejecutar:

```bash
python -m server.servidor
```

El servidor queda escuchando conexiones en:

```text
0.0.0.0:5000
```

### Terminal 2: iniciar el primer cliente

```bash
python -m client.cliente
```

Ingresar las credenciales de un usuario registrado.

### Terminal 3: iniciar otro cliente

```bash
python -m client.cliente
```

Se pueden abrir varias instancias del cliente para comprobar la comunicación simultánea.

## 8. Pruebas realizadas

Se realizaron pruebas funcionales para verificar el comportamiento del sistema.

| Prueba | Resultado |
|---|---|
| Inicio del servidor TCP | Correcto |
| Conexión de clientes | Correcto |
| Conexión simultánea de varios clientes | Correcto |
| Autenticación de usuarios registrados | Correcto |
| Rechazo de credenciales incorrectas | Correcto |
| Comunicación entre cliente y servidor | Correcto |
| Comando `/hora` | Correcto |
| Comando `/usuarios` | Correcto |
| Comando `/todos` | Correcto |
| Comando `/repos` | Correcto |
| Comando `/followers` | Correcto |
| Comando `/adios` | Correcto |
| Cierre y limpieza de conexiones | Correcto |

También se verificó la consulta de repositorios de GitHub y su almacenamiento en SQLite.

## 9. Dependencias

Las bibliotecas externas utilizadas se encuentran registradas en `requirements.txt`.

Para instalarlas:

```bash
python -m pip install -r requirements.txt
```

El archivo se generó utilizando:

```bash
pip freeze > requirements.txt
```

## 10. Estado actual del proyecto

Se encuentran implementadas y probadas las funcionalidades principales solicitadas en el trabajo integrador:

- Servidor TCP.
- Clientes concurrentes.
- Autenticación mediante SQLite.
- Comunicación bidireccional.
- Procesamiento de comandos.
- Integración con la API de GitHub.
- Almacenamiento de repositorios y seguidores.
- Difusión de mensajes a todos los clientes conectados.
- Listado de usuarios conectados.
- Desconexión controlada de clientes.

## 11. Autora

Proyecto desarrollado por Jeimmy Ortiz como trabajo integrador de la materia **Programación sobre Redes**.

Repositorio en GitHub:

https://github.com/jeimmy19/tp-integrador-redes
