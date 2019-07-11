from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('jobs/ship_date/', JobsView.as_view(), name='jobs'),
    path('bids/price/', BidsView.as_view(), name='bids'),
]