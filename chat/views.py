from django.shortcuts import render, redirect
from .forms import *


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = SignUpForm()
    context = {"form": form}
    return render(request, "chat/signup.html", context)
