from .base import *  # NOQA
from .base import BASE_DIR
from .base import env


SECRET_KEY = "django-insecure-c^ll47@0_5oy53txbjw7$lp^5bs*va5s6((g*3+_!2e4l8h7tz"

DEBUG = env.bool("DJANGO_DEBUG", default=True)

ALLOWED_HOSTS = ["*"]

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": str(BASE_DIR.path("db.sqlite3")),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

INSTALLED_APPS += ["django_extensions"]  # NOQA F405
