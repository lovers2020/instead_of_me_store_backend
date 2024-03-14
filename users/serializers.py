from rest_framework import serializers

from users.models import User


class PulblicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "username", "gender")


class PrivateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
