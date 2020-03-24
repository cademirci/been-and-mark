from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone # I use this datetime instead

class Place(models.Model):
    created = models.DateTimeField(default=timezone.now)
    place_type = models.CharField(max_length=100, default="Coffee Shop")
    name = models.CharField(max_length=100, default="No Name")
    latitude = models.FloatField(null=False, default=39.49079)
    longitude = models.FloatField(null=False, default=26.33685)
    notes = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="/place_pictures/iconbl.png", upload_to="place_pictures", null=True)

    def __str__(self):
        return self.name
