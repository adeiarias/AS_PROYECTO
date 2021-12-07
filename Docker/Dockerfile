# imagen base
FROM python:3

# la variable de entorno garantiza que la salida de python se envíe directamente a la terminal 
# sin que se almacene primero en el búfer
ENV PYTHONBUFFERED 1

# directorio para almacenar el código fuente de la aplicación
RUN mkdir /code

#copiar el código de la aplicación a la carpeta
COPY ./app_cliente /code

# cambiar al directorio /app para que todo se ejecute desde aquí
WORKDIR /code

# instalar todas las dependencias necesarias con pip
RUN pip install -r requirements.txt
