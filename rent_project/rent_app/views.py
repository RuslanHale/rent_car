from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .models import Car, Deal


class CarList(ListView):
    model = Car
    context_object_name = 'cars'


class CarDetail(DetailView):
    model = Car
    context_object_name = "car"
    template_name = "rent_app/car.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = self.object.get_details()
        return context


class CarCreate(CreateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("cars")


class CarUpdate(UpdateView):
    model = Car
    fields = "__all__"
    success_url = reverse_lazy("cars")


class CarDelete(DeleteView):
    model = Car
    context_object_name = "car"
    success_url = reverse_lazy("cars")


class DealList(ListView):
    model = Deal
    context_object_name = 'deals'


class DealDetail(DetailView):
    model = Deal
    context_object_name = "deal"
    template_name = "rent_app/deal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['details'] = self.object.get_details()
        return context


class DealCreate(CreateView):
    model = Deal
    fields = "__all__"
    success_url = reverse_lazy("deals")


class DealUpdate(UpdateView):
    model = Deal
    fields = "__all__"
    success_url = reverse_lazy("deals")


class DealDelete(DeleteView):
    model = Deal
    context_object_name = "deal"
    success_url = reverse_lazy("deals")