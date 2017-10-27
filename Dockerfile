FROM python:3

MAINTAINER Cory Sabol
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .

