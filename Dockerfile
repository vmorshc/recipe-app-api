FROM python:3.10-rc-alpine
MAINTAINER morshc45

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt 
RUN pip install -r /requirements.txt 

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user