# 🚀 FastAPI Backend - Clean Architecture

Este proyecto implementa una API con **FastAPI** siguiendo los principios de **Clean Architecture** y **Onion Architecture**. La estructura permite escalar y mantener el código de forma modular.

---

## 📂 Estructura de Carpetas

```
src/
│── api/                  # Controladores de la API
│   ├── v1/               # Version 1 de la API
│   │   ├── routes/       # Módulos de rutas
│   │   │   ├── user_routes.py
│   │   │   ├── product_routes.py
│   │   │   ├── order_routes.py
│   ├── v2/               # Version 2 de la API (ejemplo de versión futura)
│   │   ├── routes/
│   │   │   ├── user_routes.py
│   ├── health.py         # Endpoint de Health Check
│
│── core/                 # Configuración y lógica de negocio principal
│   ├── config.py         # Variables de configuración
│   ├── database.py       # Conexión a la base de datos
│
│── domain/               # Modelos de dominio
│   ├── entities/         # Entidades de negocio
│   │   ├── user.py
│   │   ├── product.py
│   ├── repositories/     # Interfaces de repositorios
│   │   ├── user_repository.py
│
│── infrastructure/       # Implementaciones concretas de infraestructura
│   ├── repositories/     # Implementaciones de acceso a datos
│   │   ├── user_repository_impl.py
│
│── main.py               # Punto de entrada de la aplicación
│
│── requirements.txt      # Dependencias del proyecto
```

---

## 📜 Explicación de Carpetas

- **`api/`**: Contiene los controladores y rutas organizadas por versiones (`v1/`, `v2/`).
- **`core/`**: Contiene configuraciones globales como la conexión a la base de datos.
- **`domain/`**: Define las entidades del negocio y las interfaces de repositorios.
- **`infrastructure/`**: Implementaciones concretas de repositorios y acceso a datos.
- **`main.py`**: Archivo principal que inicia la aplicación y registra los controladores.

---

## 🛠 Instalación y Configuración

### 🔹 1. Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 🔹 2. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 🔹 3. Instalar dependencias
```bash
pip install -r requirements.txt
py -m pip install uvicorn
py -m pip install python-jose[cryptography]
```

---

## 🚀 Ejecución de la aplicación

```bash
uvicorn src.main:app --reload
py -m uvicorn src.main:app --reload

```

Por defecto, el servidor se ejecuta en **http://127.0.0.1:8000**

---

C

### 🔹 Health Check (Verifica si el backend está operativo)
```bash
GET http://127.0.0.1:8000/health
```
**Respuesta esperada:**
```json
{"status": "ok"}
```

### 🔹 Usuarios (Ejemplo de `v1`)
```bash
GET http://127.0.0.1:8000/api/v1/user/{user_id}
```

---

## 📖 Documentación con Swagger

Una vez ejecutado el servidor, accede a la documentación automática de la API en:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

---

## Docker

Para agregar dependencias ejecutar primero py -m pip freeze > requirements.txt 

- **Contruir Imagen**: docker build -t my-fastapi-app .
- **Correr Contenedor**: docker run --env-file .env -p 8000:8000 my-fastapi-app
- **Con docker-compose**: docker-compose up --build

---

## 📌 Próximos Pasos

✅ Agregar autenticación con **OAuth2** o **JWT**.
✅ Implementar base de datos con **SQLAlchemy** y **PostgreSQL**.
✅ Desplegar en **Docker** o **Kubernetes**.

---

🚀 **¡Listo para desarrollar tu backend con FastAPI y Clean Architecture!** 🎯


