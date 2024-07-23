from django.db import models

# Create your models here.


class Car(models.Model):
    brand = models.CharField(max_length=50)
    automodel = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    seats = models.IntegerField(default=0)
    wheels = models.IntegerField(default=0)
    fuel_capacity = models.IntegerField(default=0)

    def __str__(self):
        return self.brand
