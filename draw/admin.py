from django.contrib import admin
from .models import Participant

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'token_number','phone_number','home_parish']
