from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework import response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import PrivateUserSerializer


class Me(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user)
        return response.Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = PrivateUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = serializer.save()
            serializer = PrivateUserSerializer(user)
            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)


class Users(APIView):

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise exceptions.ParseError
        serializer = PrivateUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = PrivateUserSerializer(user)

            return response.Response(serializer.data)
        else:
            return response.Response(serializer.errors)


class PublicUser(APIView):

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound
        serializer = PrivateUserSerializer(user)
        print(serializer.data)
        return response.Response(serializer.data)
