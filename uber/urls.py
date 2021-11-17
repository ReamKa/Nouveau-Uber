
from django.contrib import admin
from django.urls import path, include

from payment.views import TestView
#from rideRequest.views import PriceEstimateList,PriceEstimateDetail,TimeEstimateDetail,TimeEstimateList

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('rideRequest/',include('rideRequest.urls')),
]
