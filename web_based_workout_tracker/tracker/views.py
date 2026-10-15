from django.shortcuts import render, redirect
from .models import Exersise

# Create your views here.

def index(request):
    return render(request, "tracker/index.html")

def add_exercise(request):

    if request.method == "POST":
        name = request.POST["exersise_name"]
        pb = request.POST["exersise_pb"]
        Exersise.objects.create(name=name, pb = pb)

        return redirect("tracker:new_exersise")

    return render(request,"tracker/new_exersise.html")