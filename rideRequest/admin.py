from django.contrib import admin

# Register your models here.

from .models import PriceEstimate
from .models import TimeEstimate
from .models import CodePromo

admin.site.register(PriceEstimate)
admin.site.register(TimeEstimate)
admin.site.register(CodePromo)
