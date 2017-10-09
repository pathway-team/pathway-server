FROM python:3

MAINTAINER Cory Sabol

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# install things from apt
# install postgresql
RUN apt-get install -y libpq-dev postgresql postgresql-contrib
COPY db_conf.sh ./
RUN sh db_conf.sh

COPY . .

CMD ['python']
