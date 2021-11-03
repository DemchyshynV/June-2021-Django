FROM python:3.9-alpine

MAINTAINER SomeDev

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache --virtual ..build-deps gcc musl-dev mariadb-dev
# for Pillow
RUN apk add jpeg-dev zlib-dev libjpeg

RUN mkdir /app
WORKDIR /app

RUN adduser -D user
USER user

ENV PATH="/home/user/.local/bin:${PATH}"
RUN python -m pip install --upgrade pip && pip install --user pipenv

#COPY ./Pipfile* /tmp/
#RUN cd /tmp && pipenv lock --requirements > requirements.txt && pip install --user -r requirements.txt

COPY ./requirements.txt /tmp/
RUN cd /tmp && pip install --user -r requirements.txt
