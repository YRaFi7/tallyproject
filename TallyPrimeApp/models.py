from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.


    
class CreateStockGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)
    

class CreateStockCateg(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    

    
    
    
class CreateGodown(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    
    
class CreateEmployeeGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    
class Price_level(models.Model):
    number=models.IntegerField()
    
class UnitCrt(models.Model):
    type=models.CharField(max_length=100,null=True)
    symbol=models.CharField(max_length=20,null=True)
    formal_name=models.CharField(max_length=50,null=True)
    uqc=models.CharField(max_length=50,null=True)
    decimal=models.IntegerField(null=True)
    first_unit=models.CharField(max_length=50,null=True)
    conversion=models.CharField(max_length=30,null=True)
    second_unit=models.CharField(max_length=30,null=True)
    
class pancin(models.Model):
    pan=models.CharField(max_length=30)
    cin=models.CharField(max_length=30)
    
class cost(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    