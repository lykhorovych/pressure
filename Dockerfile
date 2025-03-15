FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE 1

RUN apt update -y

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# Додаємо права на виконання для start.sh
RUN chmod +x start.sh

ENTRYPOINT ["/bin/bash", "./start.sh"]
