from django.urls import path
from rideRequest import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('PriceEstimate',views.PriceEstimateList.as_view()),
    path('TimeEstimate',views.TimeEstimateList.as_view()),
    path('CodePromo',views.CodePromoList.as_view())

]