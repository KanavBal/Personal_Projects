from django.contrib import admin
from .models import Exersise

class ExersiseAdmin(admin.ModelAdmin):
    list_display = ("name", "pb")

# Register your models here.
admin.site.register(Exersise, ExersiseAdmin)