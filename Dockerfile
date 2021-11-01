FROM python:3.10
LABEL maintainer="andresmm@outlook.com"

WORKDIR /vin
COPY poetry.lock pyproject.toml /vin/

RUN apt-get update \
  # Librerías necesarias para opencv
  && apt-get install ffmpeg libsm6 libxext6 -y \
  && pip3 install poetry \
  && useradd --create-home --shell /bin/bash vin_user

COPY . /vin

USER vin_user

# Hacemos lo siguiente para que poetry no cree otro entorno virtual;
# al estar en docker, ya estamos en uno.
RUN  poetry config virtualenvs.create true \
  && poetry install --no-interaction

ENTRYPOINT ["./docker-entrypoint.sh"]