from django.db import models
from rest_framework import serializers
from .models import PriceEstimate, TimeEstimate, CodePromo

class PriceEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceEstimate
        fields=('id','start_latitude','start_longitude','end_latitude','end_longitude')

class TimeEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeEstimate
        fields = ('id','start_latitude','start_longitude')

class CodePromoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodePromo
        fields = ('id','code_promo')