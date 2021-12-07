from django.shortcuts import render
from rest_framework import generics, status, views

from . import models
from . import serializers


# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
