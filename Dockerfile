ARG VERSION=3.10
FROM python:$VERSION
LABEL maintainer="andresmm@outlook.com"

RUN  apt-get update \
  # Librerías necesarias para opencv
  && apt-get install ffmpeg libsm6 libxext6 -y \
#  && pip3 install poetry \
  && useradd --create-home --shell /bin/bash vin_user \
  && mkdir -p /app/test/ /__w/IV/IV \
  && chown -R vin_user:vin_user /app/test \
  # para Github Actions
  && chown -R vin_user:vin_user /__w/

USER vin_user
WORKDIR /app/test

COPY poetry.lock pyproject.toml /app/test/

ENV PATH="$PATH:/home/vin_user/.local/bin"

RUN  curl -sSL https://install.python-poetry.org | python3 - \
  && poetry config virtualenvs.create false \
  && poetry install --no-interaction

ENTRYPOINT ["poetry", "run", "task", "test"]