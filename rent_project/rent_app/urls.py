from django.urls import path
from .views import CarList, CarDetail, CarCreate, CarUpdate, CarDelete, DealList

urlpatterns = [
    path('', CarList.as_view(), name= "cars"),
    path("car/<int:pk>/", CarDetail.as_view(), name="car"),
    path('car-create/', CarCreate.as_view(), name='car-create'),
    path("car-update/<int:pk>/", CarUpdate.as_view(), name="car-update"),
    path('car-delete/<int:pk>/', CarDelete.as_view(), name='car-delete'),
    path('deals/', DealList.as_view(), name="deals"),
]
