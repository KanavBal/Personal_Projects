from django.contrib import admin
from .models import Exercise, Workout, WorkoutEntry

class ExersiseAdmin(admin.ModelAdmin):
    list_display = ("name", "pb")

class workoutEntryAdmin(admin.ModelAdmin):
    list_display = ("workout", "exercise", "weight", "reps")

class workoutAdmin(admin.ModelAdmin):
    list_display = ("id", "date")

# Register your models here.
admin.site.register(Exercise, ExersiseAdmin)
admin.site.register(Workout, workoutAdmin)
admin.site.register(WorkoutEntry, workoutEntryAdmin)