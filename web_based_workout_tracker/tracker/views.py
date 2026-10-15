from django.shortcuts import render, redirect
from .models import Exercise

# Create your views here.

def index(request):
    return render(request, "tracker/index.html")

def add_exercise(request):

    if request.method == "POST":
        name = request.POST["exercise_name"]
        pb = request.POST["exercise_pb"]
        Exercise.objects.create(name=name, pb = pb)

        return redirect("tracker:new_exercise")

    return render(request,"tracker/new_exercise.html", {
        "exercises": Exercise.objects.all()
    })

def add_workout(request):
    return render(request, "tracker/new_workout.html")
