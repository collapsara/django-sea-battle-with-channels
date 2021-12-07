import logging

from django.shortcuts import render
from rest_framework import generics, status, views

from .services import SeaField
# Create your views here.

def index(request):
    sea_field = SeaField(10)
    sea_field_opponent = SeaField(10)
    for row in sea_field.field:
        print(row)
    return render(request, 'index.html', {"field": sea_field.field, "field_opponent": sea_field_opponent.field})
