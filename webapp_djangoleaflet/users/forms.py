from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from been_and_mark.models import Place

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class PlaceCreationForm(ModelForm):
    latitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'latField'}))
    longitude = forms.FloatField(widget=forms.TextInput(attrs={'id': 'lngField'}))
    image = forms.ImageField()

    class Meta:
        model = Place
        fields = ['place_type', 'name', 'latitude', 'longitude', 'image', 'notes']
