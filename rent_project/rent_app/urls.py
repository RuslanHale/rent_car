from django.urls import path

from .views import (CarCreate, CarDelete, CarDetail, CarList, CarUpdate,
                    DealCreate, DealDelete, DealDetail, DealList, DealUpdate)

urlpatterns = [
    path('', CarList.as_view(), name= "cars"),
    path("car/<int:pk>/", CarDetail.as_view(), name="car"),
    path('car-create/', CarCreate.as_view(), name='car-create'),
    path("car-update/<int:pk>/", CarUpdate.as_view(), name="car-update"),
    path('car-delete/<int:pk>/', CarDelete.as_view(), name='car-delete'),
    path('deals/', DealList.as_view(), name="deals"),
    path("deal/<int:pk>/", DealDetail.as_view(), name="deal"),
    path('deal-create/', DealCreate.as_view(), name='deal-create'),
    path("deal-update/<int:pk>/", DealUpdate.as_view(), name="deal-update"),
    path('deal-delete/<int:pk>/', DealDelete.as_view(), name='deal-delete'),
]
