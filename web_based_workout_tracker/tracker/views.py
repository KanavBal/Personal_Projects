from django.shortcuts import render, redirect
from .models import Exercise, Workout, WorkoutEntry
from .forms import RegisterForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, authenticate
# Create your views here.

def start(request):
    return render(request, "tracker/start.html")

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

    if request.method == "POST":
        date = request.POST["date"]
        workout = Workout.objects.create(date=date)

        exercise_ids = request.POST.getlist("exercise")
        weights = request.POST.getlist("weight")
        reps = request.POST.getlist("reps")

        for exercise_id, weight, rep in zip(exercise_ids,weights,reps):
            exercise = Exercise.objects.get(id=exercise_id)

            WorkoutEntry.objects.create(
                workout=workout,
                exercise=exercise,
                weight=float(weight),
                reps=int(rep)
            )

        return redirect("tracker:index")

    return render(request, "tracker/new_workout.html", {
        "exercises": Exercise.objects.all()
    })

def view_workout(request):
    workouts = Workout.objects.all()
    data = []
    for workout in workouts:
        sets = WorkoutEntry.objects.filter(workout=workout)
        data.append({"date":workout.date, "sets":sets})

    return render(request,"tracker/view_workout.html", {
        "workouts": data
    })

def login(request):
    return render(request, "registration/login.html")

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('tracker:index')
    else:
        form = RegisterForm()

    return render(request, 'registration/signup.html', {'form':form})