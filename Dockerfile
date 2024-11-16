# Dockerfile
FROM python:3.9-slim

# Configuración del directorio de trabajo
WORKDIR /app

# Copia de los archivos del proyecto
COPY . /app

# Instalación de las dependencias
RUN pip install -r requirements.txt

# Comando por defecto para ejecutar el programa principal
CMD ["python", "main.py"]
