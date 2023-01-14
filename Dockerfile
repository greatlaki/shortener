FROM python:3.11.1-slim

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.3.0

WORKDIR /code
COPY pyproject.toml poetry.lock ./

COPY src /code/
COPY bin ./bin/
RUN chmod 777 /code/bin/entrypoint.sh

RUN pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-root --only main

ENTRYPOINT ["bin/entrypoint.sh"]