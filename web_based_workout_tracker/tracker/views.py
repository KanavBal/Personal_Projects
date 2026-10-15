from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "tracker/index.html")

def new_exersise(request):
    return render(request, "tracker/new_exersise.html")