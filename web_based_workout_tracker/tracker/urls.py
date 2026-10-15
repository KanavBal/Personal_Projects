from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.index, name="index"),
    path("new_exercise", views.add_exercise, name="new_exercise"),
]