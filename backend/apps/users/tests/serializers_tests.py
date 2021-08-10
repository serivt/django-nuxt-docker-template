import pytest
from apps.users.serializers import UserSerializer
from mixer.backend.django import mixer

from django.conf import settings

pytestmark = pytest.mark.django_db


class TestUserSerializer(object):
    @pytest.mark.unit
    def test_serializer_model(self):
        with mixer.ctx(commit=False):
            user = mixer.blend(settings.AUTH_USER_MODEL)
            serializer = UserSerializer(user)
            assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self):
        user = {"username": "admin"}
        serializer = UserSerializer(data=user)
        assert serializer.is_valid(), serializer.errors
        assert serializer.errors == {}
