from django.shortcuts import render
from .models import *
from rest_framework import generics, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Jobs(APIView):
    def get(self, request):
        jobs = Jobs.objects.all()
        result = list(jobs.values())
        for x in range(0, len(result)):
            for y in range(x+1, len(result)):
                if result[x].ship_date > result[y].ship_date:
                    result[x].ship_date, result[y].ship_date = result[y].ship_date, result[x].ship_date 
        return Response(result, status=status.HTTP_200_OK)
    
class Bids(APIView):
    def get(self, request):
        Bids = Bids.objects.all()
        result = list(jobs.values())
        for x in range(0, len(result)):
            for y in range(x+1, len(result)):
                if result[x].price > result[y].price:
                    result[x].price, result[y].price = result[y].price, result[x].price 
        return Response(result, status=status.HTTP_200_OK)