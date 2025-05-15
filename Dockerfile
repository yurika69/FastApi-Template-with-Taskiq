FROM python:3-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/code
COPY . /app/code/

RUN pip install -r req.txt