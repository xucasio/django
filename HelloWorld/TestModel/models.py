# models.py
from django.db import models
 
class Test(models.Model):
    price = models.IntegerField()