from rest_framework import serializers

from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = ("pk", "username", "first_name", "last_name", "is_active")
