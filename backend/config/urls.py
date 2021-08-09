"""URL Configuration """
import os

from config.utils import get_apps_names

from django.conf import settings
from django.contrib import admin
from django.urls import include, path


def get_apps_urls() -> list:
    patterns = []
    apps = get_apps_names(settings.APPS_DIR)
    for app in apps:
        urls = settings.APPS_DIR.path(app).path("urls.py")
        if os.path.exists(urls):
            module = __import__("apps.%s" % app, fromlist=["urls"])
            app_name = getattr(getattr(module, "urls"), "app_name")
            patterns.append(path("%s/" % app_name, include("apps.%s.urls" % app)))
    return patterns


urlpatterns = [
    path(
        "api/",
        include(
            [
                path("admin/", admin.site.urls),
            ]
            + get_apps_urls()
        ),
    )
]
