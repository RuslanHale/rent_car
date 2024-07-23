from django.shortcuts import render, get_object_or_404
from .models import Car
from django.http import HttpResponse
# Create your views here.


def index(request):
    car_list = Car.objects.order_by("brand")
    context = {
        "car_list": car_list,
    }
    return render(request, 'rent_app/index.html', context)


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    car_attrs = [i for i in car.__dict__.keys() if i != 'id' and i != '_state']
    context = {
        "car": car,
        "car_attrs": car_attrs,
    }
    return render(request, "rent_app/detail.html", context)
