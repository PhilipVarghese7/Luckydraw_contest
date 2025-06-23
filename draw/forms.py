from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name','phone_number','home_parish']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number', 'class': 'form-control'}),
            'home_parish': forms.TextInput(attrs={'placeholder': 'Enter your Home parish', 'class': 'form-control'}),
        }
