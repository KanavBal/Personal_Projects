from django.contrib import admin
from .models import Exercise

class ExersiseAdmin(admin.ModelAdmin):
    list_display = ("name", "pb")

# Register your models here.
admin.site.register(Exercise, ExersiseAdmin)