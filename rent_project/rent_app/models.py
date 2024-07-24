from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.CharField(max_length=50)
    automodel = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    seats = models.IntegerField(default=0)
    wheels = models.IntegerField(default=0)
    fuel_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.brand

    def get_details(self):
        return {
            'brand': self.brand,
            'automodel': self.automodel,
            'color': self.color,
            'number': self.number,
            'seats': self.seats,
            'wheels': self.wheels,
            'fuel_capacity': self.fuel_capacity,
        }