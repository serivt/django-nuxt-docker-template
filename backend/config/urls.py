"""URL Configuration """
import os

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from config.utils import get_local_apps


def get_apps_urls() -> list:
    patterns = []
    apps = get_local_apps(settings.APPS_DIR)
    for app in apps:
        urls = settings.APPS_DIR.path(app).path("urls.py")
        if os.path.exists(urls):
            module = __import__("apps.%s" % app, fromlist=["urls"])
            app_prefix = getattr(getattr(module, "urls"), "app_prefix")
            patterns.append(path(app_prefix, include("apps.%s.urls" % app)))
    return patterns


urlpatterns = [
    path("api/", include([
        path("admin/", admin.site.urls),
    ] + get_apps_urls()))
]
