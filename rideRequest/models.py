from django.db import models
from django.db.models.base import ModelState

#GET price estimates
class PriceEstimate(models.Model):
    start_latitude = models.FloatField() #dans le formulaire, il sera obligatoire d'utiliser NumberInput
    start_longitude = models.FloatField()
    end_latitude = models.FloatField()
    end_longitude = models.FloatField()
    def __str__(self) -> float:
        return self.start_latitude

#GET time estimates
class TimeEstimate(models.Model):
    start_latitude = models.FloatField()
    start_longitude = models.FloatField()
    def __str__(self) -> float:
        return self.start_latitude

#PATCH un code promo 
class CodePromo(models.Model):
    code_promo = models.CharField(max_length=5)
    def __str__(self) -> str:
        return self.code_promo


