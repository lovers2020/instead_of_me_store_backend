from django.urls import path

from users import views


urlpatterns = [
    path("", views.Users.as_view()),
    path("me", views.Me.as_view()),
    path("change-password", views.ChangePassword.as_view()),
    path("log-in", views.Login.as_view()),
    path("log-in2", views.LogIn2.as_view()),
    path("log-out", views.Logout.as_view()),
    path("@<str:username>", views.PublicUser.as_view()),
]
