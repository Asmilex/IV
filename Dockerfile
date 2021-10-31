FROM python:3.10
LABEL maintainer="andresmm@outlook.com"

WORKDIR /vin
COPY poetry.lock pyproject.toml /vin/

RUN apt-get update \
  # Librerías necesarias para opencv
  && apt-get install ffmpeg libsm6 libxext6 -y \
  && pip3 install poetry \
  # Hacemos lo siguiente para que poetry no cree otro entorno virtual;
  # al estar en docker, ya estamos en uno.
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction

COPY . /vin

ENTRYPOINT ["./docker-entrypoint.sh"]