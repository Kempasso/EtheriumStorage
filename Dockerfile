FROM python:3.10.8
WORKDIR /app

COPY . /app
RUN apt-get update && \
    apt-get install -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"

RUN poetry config virtualenvs.create false  \
    && poetry lock --no-update  \
    && poetry install --no-dev --no-root