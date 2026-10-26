from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exercise(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="exercises")
    name = models.CharField()
    pb = models.IntegerField()

    def __str__(self):
        return f"Name:{self.name}, Personal Best: {self.pb}"

class Workout(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="workouts")
    date = models.DateField()

    def __str__(self):
        return f"Date of workout {self.date}"

class WorkoutEntry(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name="workout")
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, related_name="exercise")
    weight = models.IntegerField()
    reps = models.IntegerField()

    def __str__(self):
        return f"Workout nr. {self.workout.id}:\n Exercise: {self.exercise.name}\n Weight: {self.weight}\n Reps: {self.reps}"