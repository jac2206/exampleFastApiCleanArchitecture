# Etapa 1: Construcción
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Etapa 2: Imagen final
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

# python:3.11-alpine
# # Usa una imagen oficial de Python como base
# FROM python:3.11

# # Establece el directorio de trabajo en el contenedor
# WORKDIR /app

# # Copia los archivos de la aplicación al contenedor
# COPY . .

# # Instala dependencias
# RUN pip install --no-cache-dir -r requirements.txt

# # # Definir variables de entorno
# # ENV DB_HOST="mydatabase.com"
# # ENV DB_USER="admin"
# # ENV DB_PASSWORD="mypassword"

# # Exponer el puerto en el que correrá la app
# EXPOSE 8000

# # Comando para ejecutar la aplicación
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
