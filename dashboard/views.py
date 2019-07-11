from django.shortcuts import render
from .models import *
from rest_framework import generics, status, exceptions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class JobsView(APIView):
    def get(self, request):
        jobs = Jobs.objects.all()
        result = list(jobs.values())
        for x in range(0, len(result)):
            for y in range(x+1, len(result)):
                if result[x]['ship_date'] > result[y]['ship_date']:
                    result[x], result[y] = result[y], result[x]
        return Response(result, status=status.HTTP_200_OK)
    
class BidsView(APIView):
    def get(self, request):
        bids = Bids.objects.all()
        result = list(bids.values())
        for x in range(0, len(result)):
            for y in range(x+1, len(result)):
                if result[x]['price'] > result[y]['price']:
                    result[x], result[y] = result[y], result[x] 
        return Response(result, status=status.HTTP_200_OK)