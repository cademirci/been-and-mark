from django.shortcuts import render
from .models import Place

def home(request):
    context = { 'points': Place.objects.all() }
    return render(request, 'been_and_mark/home.html', context)
