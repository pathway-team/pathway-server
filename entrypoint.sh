#!/bin/sh

# migrate db
echo "Apply db migrations"
python3 manage.py makemigrations
python3 manage.py migrate

# start the server
gunicorn -b 0.0.0.0:8000 server.wsgi
