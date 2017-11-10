# Pathway-Server

This is the application which handles all of the backend work
for the Pathway Android application. It's built using; Python3,
Django, PostgreSQL, Gunicorn, Docker, and is deployed using
AWS Elastic Beanstalk.


## Developing/Contributing
1. Clone this repository with `git clone https://github.com/pathway-team/pathway-server`
    * `cd pathway-server`
2. Install Docker and Docker Compose (if you don't have them already)
    * If you're on linux; `sudo apt-get install docker.io docker-compose`
    * If you're on Windows 10; See [here](https://docs.docker.com/docker-for-windows/install/) and [here](https://docs.docker.com/compose/install/)
3. Start up the docker containers with `docker-compose up`
    * show running containers with `docker ps`
4. If everything worked, you should be able to simply make changes to the web app
    source code in `/pathwayserv` (on a dedicated branch or fork of course) and then
    re-run the containers with `docker-compose up`.
5. The application should be accessible from `127.0.0.1:8000` on your host machine.

### Creating an Admin Account for Dev Purposes
You may want to have an admin account in the database for development and testing
purposes. You can create one by following the below steps;

1. Make sure the container is up and running, if not run `docker-compose up`
2. If this is a fresh run then you will need to migrate the database.
    * Run `docker-compose exec web python manage.py makemigrations`
    * Then run `docker-compose exec web python manage.py migrate`
3. Now you can create a superuser account on the db
    * Run `docker-compose exec web python manage.py createsuperuser`
    * Follow the prompts in the terminal
4. Goto `127.0.0.1:8000/admin` in your browser and try to log in

# TODO:
1. Finish this README
