from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "tracker"

urlpatterns = [
    path("", views.start, name="start"),
    path("home", views.index, name="index"),
    path("new_exercise", views.add_exercise, name="new_exercise"),
    path("workout", views.add_workout, name="new_workout"),
    path("view_workout", views.view_workout, name="view_workout"),
    path('', include("django.contrib.auth.urls")),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"),name="login"),
    path("signup", views.signup, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]