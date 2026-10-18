from django.urls import path
from . import views

app_name = "tracker"

urlpatterns = [
    path("", views.index, name="index"),
    path("new_exercise", views.add_exercise, name="new_exercise"),
    path("workout", views.add_workout, name="new_workout"),
    path("view_workout", views.view_workout, name="view_workout")
]