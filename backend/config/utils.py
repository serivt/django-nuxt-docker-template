from os import listdir
from os.path import isfile


def get_local_apps(apps_dir):
    return ["apps.%s" % d for d in listdir(apps_dir) if not isfile(apps_dir.path(d))]


def get_apps_names(apps_dir):
    return [str(d) for d in listdir(apps_dir) if not isfile(apps_dir.path(d))]
