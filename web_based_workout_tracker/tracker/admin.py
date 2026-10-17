from django.contrib import admin
from .models import Exercise, Workout, WorkoutEntry

class ExersiseAdmin(admin.ModelAdmin):
    list_display = ("name", "pb")

# Register your models here.
admin.site.register(Exercise, ExersiseAdmin)
admin.site.register(Workout)
admin.site.register(WorkoutEntry)