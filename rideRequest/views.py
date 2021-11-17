#from django.shortcuts import render
from rest_framework import generics
from .models import PriceEstimate, TimeEstimate,CodePromo
from .serializers import CodePromoSerializer, PriceEstimateSerializer, TimeEstimateSerializer
#from UberDeLaHess.uber.rideRequest import serializers

#Permet de creer un price estimate et de voir une liste de tous les price estimate crées
class PriceEstimateList(generics.ListCreateAPIView):
    queryset = PriceEstimate.objects.all()
    serializer_class = PriceEstimateSerializer

#Permet de voir un price estimate en particulier, de le update ou de le delete
class PriceEstimateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PriceEstimate.objects.all()
    seriializer_class = PriceEstimateSerializer

#Permet de creer un estimate DU TEMPS et de voir une liste de tous les estimate crées
class TimeEstimateList(generics.ListCreateAPIView):
    queryset = TimeEstimate.objects.all()
    serializer_class = TimeEstimateSerializer

#Permet de voir un estimate DE TEMPS en particulier, de le update ou de le delete
class TimeEstimateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeEstimate.objects.all()
    serializer_class = TimeEstimateSerializer

class CodePromoList(generics.ListCreateAPIView):
    queryset = CodePromo.objects.all()
    serializer_class = CodePromoSerializer



