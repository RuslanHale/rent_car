from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.


class CarList(ListView):
    model = Car
    context_object_name = 'cars'


class CarDetail(DetailView):
    model = Car
    context_object_name = "car"
    template_name = "rent_app/car.html"
