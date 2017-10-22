FROM python:3

MAINTAINER Cory Sabol

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# install things from apt
# install postgresql
RUN apt-get update
RUN apt-get install -y libpq-dev postgresql
# need to change to user postgres
USER postgres
COPY ./setup_cmds.sql .
# Start the postgres daemon
# create and configure the db for django to use
RUN /etc/init.d/postgresql start && \
    psql -f setup_cmds.sql

# exit the postgres user
RUN exit

RUN gunicorn --help

# Expose the web app port 8000
EXPOSE 8000
# Start the application
CMD ["gunicorn server.wsgi"]

