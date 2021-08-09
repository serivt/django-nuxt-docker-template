# A Django+Nuxt project template using Docker

It's a simple [Django](https://www.djangoproject.com/) project that uses [Django REST framework](http://www.django-rest-framework.org/) for the backend and [Nuxt.js](https://nuxtjs.org/) with [Vuetify.js](https://vuetifyjs.com/) for the frontend. The template has a basic auth system with [JWT](https://jwt.io/) and makes use of docker to provide a production-ready container configurable via environment variables.

The main idea is to replace Django's default template system with Nuxt.js and only fetch data using API, totally avoiding using the [Django Template Language](https://docs.djangoproject.com/en/3.2/ref/templates/language/). The backend runs through Gunicorn and the frontend runs on separate [Node.js](https://nodejs.org/) server, and communicated by a reverse proxy server ([Nginx](https://www.nginx.com/) in this case, but it could also work with [Caddy](https://caddyserver.com/) for example).

It uses python3.8, Django 3.2.4, Nuxt 2.15 and requires [Docker](https://www.docker.com/).

## Directory Structure
```
├── backend/ (Django project folder)
|   └── apps/ (django applications)
|   └── config/ (django settings)
|   └── requirements/ (pip requirements)
|   └── manage.py
├── docker/
├── frontend/ (Nuxt.js project folder)
|   └── ...
├── pre-commit-config.yaml
├── site.conf (Nginx config for developement server)
├── ...
```
The project has method to auto detect apps inside ``backend/apps`` folder and it is added to INSTALLED_APPS, if this app has ``urls.py`` file then it is added to general urls as well.

All Nuxt related files are in the ``frontend`` folder, learn more about the nuxt directory structure [here](https://nuxtjs.org/docs/2.x/get-started/directory-structure).

In the docker folder there are 2 folders, one for each environment; The production environment is designed to be an image as light as possible, only with the packages strictly necessary for the application to work, whereas the development environment contains tools for debugging, testing, among others.

Also there are some files for linter and formatter config, and tools for code quality.

## How does auto-discovery of apps and urls work?
For applications: All Python modules inside the ``backend/apps`` folder that contain the apps.py file are automatically added to Django's INSTALLED_APPS.

> For each new application that you add, it is necessary to update the apps.py by modifying the name attribute, adding 'apps'. as a prefix, as follows: name = "appname" -> name = "apps.appname"

For urls: For each application in INSTALLED_APPS that contains the urls.py file, all its patterns will be added to the global urls, using the app_name prefix.

E.g:

The [user application](backend/apps/users) is automatically added to INSTALLED_APPS, and the application urls (whose app_name attribute is 'users') to the global urls, then the complete urls would be as follows:
```
METHOD /api/<app_name>/<pattern>/
POST /api/users/login/
GET /api/users/me/
```

## Environment variables
Coming soon...

## Deploy in development
In order to deploy the application with docker, you need to build the development images, and run the containers with docker-compose, just run:
```bash
$ docker build -t django-template:development -f docker/development/backend/Dockerfile .
$ docker build -t frontend-template:development -f docker/development/frontend/Dockerfile .
$ docker-compose up
```

> if you build the images with different tags, you must be also edit the ``docker-compose.yml``

The previous command will create the containers, including the nginx reverse proxy, but is necessary execute the applications server manually, for this you enter the backend and frontend containers on two different terminals and run:

```bash
$ python manage.py runserver 0.0.0.0:8000 # for backend
$ npm run dev # for frontend
```
Finally, open http://127.0.0.1:8800/ on your browser.

For auth you need to create at least one user, in backend terminal just run:
```bash
$ python manage.py createsuperuser
```

## Deploy in production
Coming soon...
