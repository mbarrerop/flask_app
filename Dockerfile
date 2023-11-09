# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Establece el directorio de trabajo en /app
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copia el contenido del directorio actual al contenedor en /app
COPY . .

# Instala las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000 (ajusta según el puerto de tu aplicación)
EXPOSE 5000

# Ejecuta la aplicación Flask cuando se inicia el contenedor
CMD gunicorn main:app -b 0.0.0.0:5000 --max-requests 100 --access-logfile - --error-logfile - --log-level info