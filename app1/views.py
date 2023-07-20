from django.shortcuts import render
from .models import Town
import random

def home(request):
    return render(request, 'home.html')

def list(request):
    items = Town.objects.all()
    context = {'items':items}
    return render(request, 'items.html', context)

def plus_id(request):
    items = Town.objects.all()
    context = {'items':items}
    for i in items:
        i.c_name = i.c_name + str(i.c_aeroport_index)
        i.save()
    return render(request, 'plus_id.html', context)