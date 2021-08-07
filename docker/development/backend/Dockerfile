FROM python:3.8-alpine3.13

RUN adduser -D python \
    && mkdir /home/python/app/ \
    && mkdir /home/python/logs

ENV DJANGO_SETTINGS_MODULE=config.settings.development

WORKDIR /home/python/app

COPY ./backend/requirements/development/requirements.txt /requirements.txt

RUN apk update \
    && pip install --upgrade pip && pip install pip-tools \
    && pip install -r /requirements.txt

RUN touch /home/python/logs/django.log

COPY ./backend .

CMD while true; do sleep 30; done;
