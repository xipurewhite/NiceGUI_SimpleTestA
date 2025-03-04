FROM python:3.12-slim
RUN pip install poetry==1.8.5
RUN poetry self update 2.1.1

WORKDIR /app
COPY . /app

RUN poetry install --no-root

EXPOSE 8080

CMD ["poetry", "run", "python", "ui_layer.py"]