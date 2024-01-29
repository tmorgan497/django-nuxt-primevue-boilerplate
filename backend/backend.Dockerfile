# backend/backend.Dockerfile

FROM python:3.12.1 AS dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY ./requirements.txt /code/
COPY . /code/backend

# RUN apt-get update && apt-get install -y cron

RUN pip install -r requirements.txt
