from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .forms import PlaceCreationForm
from been_and_mark.models import Place

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'user ({username}) created succesfully.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    context = { 'points': Place.objects.all() }
    return render(request, 'users/profile.html', context)

@login_required
def add_place(request):
    context = { 'points': Place.objects.all() }
    form = PlaceCreationForm(request.POST, request.FILES)
    place = Place(user=request.user)
    if request.method == 'POST':
        form = PlaceCreationForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            place_name = form.cleaned_data.get('name')
            image = form.cleaned_data.get('image')

            messages.success(request, f'New place ({place_name}) created succesfully.')
            return redirect('app-home')
    else:
        form = PlaceCreationForm()
    context.update({'form': form})
    return render(request, 'users/add-place.html', {'form': form})
