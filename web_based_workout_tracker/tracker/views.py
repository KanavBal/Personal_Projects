from django.shortcuts import render, redirect
from .models import Exercise, Workout, WorkoutEntry
from .forms import RegisterForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout, authenticate
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

def start(request):
    return render(request, "tracker/start.html")

@login_required
def index(request):
    return render(request, "tracker/index.html")

@login_required
def add_exercise(request):

    if request.method == "POST":
        name = request.POST["exercise_name"]
        pb = request.POST["exercise_pb"]
        Exercise.objects.create(user=request.user, name=name, pb = pb)

        return redirect("tracker:new_exercise")

    return render(request,"tracker/new_exercise.html", {
        "exercises": Exercise.objects.filter(user=request.user)
    })

@login_required
def add_workout(request):

    if request.method == "POST":
        date = request.POST["date"]
        workout = Workout.objects.create(user=request.user,date=date)

        exercise_ids = request.POST.getlist("exercise")
        weights = request.POST.getlist("weight")
        reps = request.POST.getlist("reps")

        for exercise_id, weight, rep in zip(exercise_ids,weights,reps):
            exercise = get_object_or_404(Exercise,id=exercise_id,user=request.user)
            if float(weight) > exercise.pb:
                exercise.pb = float(weight)
                exercise.save()

            WorkoutEntry.objects.create(
                workout=workout,
                exercise=exercise,
                weight=float(weight),
                reps=int(rep)
            )

        

        return redirect("tracker:index")

    return render(request, "tracker/new_workout.html", {
        "exercises": Exercise.objects.filter(user=request.user)
    })

@login_required
def view_workout(request):
    workouts = Workout.objects.filter(user=request.user)
    data = []
    for workout in workouts:
        sets = WorkoutEntry.objects.filter(workout=workout)
        data.append({"date":workout.date, "sets":sets})

    reversed_data = data[::-1]
    return render(request,"tracker/view_workout.html", {
        "workouts": reversed_data
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