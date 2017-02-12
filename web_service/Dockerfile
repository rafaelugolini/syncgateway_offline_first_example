FROM python:3.6

EXPOSE 5000

COPY ./ /usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

RUN adduser --disabled-password --gecos '' celery

ENV API_SETTINGS settings.py

ENV CELERYD_USER celery
ENV CELERYD_GROUP celery
