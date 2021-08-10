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
* DJANGO_REDIS_URL _(type: string, default: None)_ If its set, it will be used for [caches](https://docs.djangoproject.com/en/3.2/ref/settings/#caches).
* [DJANGO_DEBUG](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG) _(type: boolean, default: {production: False, development: True})_

### Only production environment
* [DJANGO_SECRET_KEY](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECRET_KEY) _(type: string, required)_
* [DJANGO_ALLOWED_HOST](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts) _(type: list, required)_
* [DJANGO_DATABASE_URL](https://github.com/jacobian/dj-database-url#url-schema) _(type: string, required)_
* [DJANGO_ATOMIC_REQUESTS](https://docs.djangoproject.com/en/3.2/ref/settings/#atomic-requests) _(type: boolean, default: False)_
* [DJANGO_CONN_MAX_AGE](https://docs.djangoproject.com/en/3.2/ref/settings/#conn-max-age) _(type: integer, default: 0)_
* [DJANGO_HTTP_X_FORWARDED_PROTO](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-proxy-ssl-header) _(type: string, default: "https")_
* [DJANGO_SECURE_SSL_REDIRECT](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-ssl-redirect) _(type: boolean, default: True)_
* [DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-hsts-include-subdomains) _(type: boolean, default: True)_
* [DJANGO_SECURE_HSTS_PRELOAD](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-SECURE_HSTS_PRELOAD) _(type: boolean, default: True)_
* [DJANGO_SECURE_CONTENT_TYPE_NOSNIFF](https://docs.djangoproject.com/en/3.2/ref/settings/#secure-content-type-nosniff) _(type: boolean, default: True)_

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
