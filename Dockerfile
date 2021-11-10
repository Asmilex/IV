FROM python:3.10
LABEL maintainer="andresmm@outlook.com"


RUN  apt-get update \
  # Librerías necesarias para opencv
  && apt-get install ffmpeg libsm6 libxext6 -y \
#  && pip3 install poetry \
  && useradd --create-home --shell /bin/bash vin_user \
  && mkdir /vin \
  && chown -R vin_user:vin_user /vin

USER vin_user
WORKDIR /vin
COPY poetry.lock pyproject.toml docker-entrypoint.sh /vin/

ENV PATH="$PATH:/home/vin_user/.local/bin"

RUN  pip3 install poetry \
  && poetry config virtualenvs.create true \
  && poetry install --no-interaction

ENTRYPOINT ["sh", "./docker-entrypoint.sh"]