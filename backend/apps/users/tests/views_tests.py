import json

import pytest
from mixer.backend.django import mixer

from django.conf import settings
from django.urls import reverse

pytestmark = pytest.mark.django_db


class TestLoginViewSet(object):
    @pytest.mark.urls("apps.users.urls")
    def test_login_ok(self, api_client):
        url = reverse("login")
        password = "thepassword"
        user = mixer.blend(settings.AUTH_USER_MODEL)
        user.set_password(password)
        user.save()
        data = {"username": user.username, "password": password}
        response = api_client.post(url, data=data)
        assert response.status_code == 200, response.content
        content = json.loads(response.content)
        assert "access" in content and "refresh" in content, response.content

    @pytest.mark.urls("apps.users.urls")
    def test_login_fail(self, api_client):
        url = reverse("login")
        user = mixer.blend(settings.AUTH_USER_MODEL)
        data = {"username": user.username, "password": "mypassword"}
        response = api_client.post(url, data=data)
        assert response.status_code == 401, response.content


class TestMeViewSet(object):
    @pytest.mark.urls("apps.users.urls")
    def test_me_unauthorized_user(self, api_client):
        url = reverse("me")
        response = api_client.get(url)
        assert response.status_code == 401, response.content

    @pytest.mark.urls("apps.users.urls")
    def test_me_authorized_user(self, auth_api_client):
        url = reverse("me")
        response = auth_api_client.get(url)
        assert response.status_code == 200, response.content
