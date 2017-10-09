FROM python:3

MAINTAINER Cory Sabol

WORKDIR /usr/src/app

COPY requirements.txt ./
#RUN pip3 install --no-cache-dir -r requirements.txt

# install things from apt
# install postgresql
RUN apt-get update
RUN apt-get install -y libpq-dev postgresql
# need to change to user postgres
RUN su - postgres
# then run the config
COPY ./db_conf.sh .
RUN sh db_conf.sh
