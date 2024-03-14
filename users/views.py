from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
import jwt, datetime
import requests

from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework import response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from django.conf import settings

from users.models import User
from users.serializers import PrivateUserSerializer, PulblicUserSerializer


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
        serializer = PulblicUserSerializer(user)
        print(serializer.data)
        return response.Response(serializer.data)


class SignUp(APIView):
    def post(self, request):
        pass


class Login(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = User.objects.filter(username=username).first()
        if not user:
            raise AuthenticationFailed("User does not exist!")
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        user = authenticate(request, username=username, password=password)
        if user:
            payload = {
                "id": user.username,
                "exp": datetime.datetime.now() + datetime.timedelta(weeks=2),
                "iat": datetime.datetime.now(),
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            return response.Response({"token": token}, status=status.HTTP_200_OK)
        else:
            return response.Response(
                {"error": "wrong password"}, status=status.HTTP_400_BAD_REQUEST
            )


class LogIn2(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return response.Response({"ok": "Welcome!"}, status=status.HTTP_200_OK)
        else:
            return response.Response(
                {"error": "wrong password"}, status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):
    def post(self, request):
        logout(request)
        return response.Response({"ok": "logout"})


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        old_password = request.data.get("old_password")
        new_password = request.data.get("new_password")

        if not old_password or not new_password:
            raise ParseError

        if user.check_password(old_password):
            user.set_password(new_password)
            user.save()
            return response.Response(status=status.HTTP_200_OK)
        else:
            return response.Response(status=status.HTTP_400_BAD_REQUEST)


# 아이디, 비밀번호 찾기
