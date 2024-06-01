FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app

# Указываем рабочую директорию, где находится main.py
WORKDIR /app/src
EXPOSE 8000

CMD ["python3", "main.py"]

