backend/
│── src/                           # Código fuente principal
│   ├── api/                       # Capa de Presentación (Interfaz de Entrada)
│   │   ├── v1/routes/             # Rutas de la API
│   │   │   └── user_routes.py
│   │   ├── dependencies.py        # Dependencias compartidas (Ej: DB, Auth)
│   │
│   ├── core/                      # Configuración y utilidades generales
│   │   ├── config.py              # Configuración del proyecto
│   │   ├── security.py            # Seguridad (JWT, OAuth2, etc.)
│   │
│   ├── domain/                    # Capa de Dominio (Reglas de Negocio y Entidades)
│   │   ├── entities/              # Entidades de dominio puro
│   │   │   └── user.py
│   │   ├── interfaces/            # Interfaces para inyección de dependencias
│   │   │   └── user_repository.py
│   │
│   ├── application/               # Capa de Aplicación (Casos de Uso y Servicios)
│   │   ├── use_cases/             # Lógica de negocio
│   │   │   └── user_service.py
│   │   ├── dtos/                  # Data Transfer Objects (DTOs)
│   │   │   └── user_dto.py        # Esquemas Pydantic para entrada/salida de datos
│   │
│   ├── infrastructure/            # Capa de Infraestructura (Persistencia y Adaptadores)
│   │   ├── repositories/          # Implementaciones concretas de repositorios
│   │   │   └── user_repository.py
│   │   ├── database.py            # Configuración de la base de datos
│   │
│   ├── main.py                    # Punto de entrada de la aplicación
│
├── requirements.txt                # Dependencias del proyecto
├── README.md                       # Documentación del proyecto


Carpeta	Descripción
api/	Define las rutas de la API y maneja la entrada/salida de datos.
core/	Configuración global, seguridad, logs y utilidades generales.
domain/	Contiene las entidades de negocio y las interfaces de repositorios.
application/	Contiene la lógica de negocio con los casos de uso y DTOs.
infrastructure/	Implementaciones concretas como persistencia en BD.

py -m uvicorn src.main:app --reload
