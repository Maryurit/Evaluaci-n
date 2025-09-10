# Imagen base
FROM python:3.10

# Info del autor
LABEL maintainer="tucorreo@dominio.com"

# Crear carpeta de trabajo
WORKDIR /app

# Copiar dependencias primero
COPY requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto 9000
EXPOSE 9000

# Comando para ejecutar el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
