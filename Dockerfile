# Versión de python
FROM python:3.10.4
# Directorio de trabajo
WORKDIR /usr/src/app    # directorio de trabajo

# copiando archivos al contenedor
COPY . .
# Instalando dependencias desde archivo requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
# Puerto en que será expuesta nuestra aplicación
#EXPOSE 5000
CMD [ "python", "scrap_something.py"]