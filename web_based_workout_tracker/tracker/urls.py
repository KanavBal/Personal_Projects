from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_exersise", views.new_exersise, name="new_exersise")
]