from .base import *  # NOQA
from .base import env

DEBUG = False

SECRET_KEY = env.str("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOST")

# Database

DATABASES = {"default": env.db("DJANGO_DATABASE_URL")}

DATABASES["default"]["ATOMIC_REQUESTS"] = env.bool("DJANGO_ATOMIC_REQUESTS", default=False)

DATABASES["default"]["CONN_MAX_AGE"] = env.int("DJANGO_DATABASE_CONN_MAX_AGE", default=0)
