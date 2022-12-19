# seleccionamos la imagen
FROM python:3.11.1-alpine3.17

# para ver el log de la app
ENV PYTHONUNBUFFERED=1

# le indicamos a docker en que directorio queremos trabajar
# los comandos que se especifiquen en el dockerhub se realizan en este directorio
WORKDIR /app

# actualizamos alpine e instalamos las dependencias necesarias 
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip

# copiamos los archivos necesarios para poder preparar el equipo
# copiamos requirements y lo mandamos al direcctorio de trabajo /app
COPY ./requirements.txt ./

RUN ["pip","install", "-r","requirements.txt"]

# copiamos el proyecto
COPY ./ ./

# ejecutamos el proyecto
# acolocamos la direcci[on] 0.0.0.0:8000 para poder tener acceso al contenedor
# CMD ["sh", "entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]