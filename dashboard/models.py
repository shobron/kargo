from django.db import models

# Create your models here.
class Shippers(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Transporters(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Jobs(models.Model):
    origin =  models.CharField(max_length=32)
    destination = models.CharField(max_length=32)
    ship_date = models.DateField()
    budget = models.FloatField()
    description = models.CharField(max_length=1024)
    status = models.CharField(max_length=32)
    shippers = models.ForeignKey(Shippers, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Bids(models.Model):
    price = models.FloatField()
    vehicle = models.CharField(max_length=32)
    description = models.CharField(max_length=1024)
    transporters = models.ForeignKey(Transporters, on_delete=models.CASCADE)
    jobs = models.ForeignKey(Jobs, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
