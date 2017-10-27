FROM python:3

MAINTAINER Cory Sabol
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . /code/

