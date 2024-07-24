from django.urls import path
from .views import CarList, CarDetail


urlpatterns = [
    path("", CarList.as_view(), name= "cars"),
    path("car/<int:pk>/", CarDetail.as_view(), name="car"),
]
