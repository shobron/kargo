from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('jobs/ship_date/)', Jobs.as_view(), name='jobs'),
    path('bids/price/)', Bids.as_view(), name='bids'),
]