import pytest
from mixer.backend.django import mixer

from django.conf import settings


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def auth_api_client(db, api_client):
    user = mixer.blend(settings.AUTH_USER_MODEL)
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
