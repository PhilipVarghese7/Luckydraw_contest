from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ParticipantForm
from .models import Participant
import random
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.http import HttpResponse



def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)

            # Auto assign token number as count + 1
            last_token = Participant.objects.count()
            participant.token_number = last_token + 1

            participant.save()
            return render(request, 'thankyou.html', {'participant': participant})
    else:
        form = ParticipantForm()
    return render(request, 'register.html', {'form': form})

def create_admin_user(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword123')
        return HttpResponse("Admin user created.")
    else:
        return HttpResponse("Admin user already exists.")

@login_required
def view_entries(request):
    participants = Participant.objects.all().order_by('token_number')
    return render(request, "entries.html", {"participants": participants})

@login_required
def pick_winner(request):
    participants = list(Participant.objects.all())
    if len(participants) >= 5:
        Participant.objects.update(is_winner=False)
        winners = random.sample(participants, 5)
        for winner in winners:
            winner.is_winner = True
            winner.save()
    return redirect("show_winner")


@login_required
def show_winner(request):
    winners = Participant.objects.filter(is_winner=True)
    return render(request, "winner.html", {"winners": winners})




