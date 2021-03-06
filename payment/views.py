from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "driver_id": "8LvWuRAq2511gmr8EMkovekFNa2848lyMaQevIto-aXmnK9oKNRtfTxYLgPq9OSt8EzAu5pDB7XiaQIrcp-zXgOA5EyK4h00U6D1o7aZpXIQah--U77Eh7LEBiksj2rahB==",
            "first_name": "UberDeLaHess",
            "last_name": "Tester",
            "email": "uber.developer+tester@example.com",
            "phone_number": "+14155550000",
            "picture": "https://d1w2poirtb3as9.cloudfront.net/16ce502f4767f17b120e.png",
            "promo_code": "ubert4544ue",
            "rating": 5,
        }
        return Response(data)
