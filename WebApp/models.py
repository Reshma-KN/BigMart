from django.db import models

# Create your models here.
class Contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
class Registerdb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email =models.EmailField(max_length=100,null=True,blank=True)
    Password = models.CharField(max_length=100,null=True,blank=True)
    Confirm_Password = models.CharField(max_length=100,null=True,blank=True)

class Cartdb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    Product_Name = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    Total_Price = models.IntegerField(null=True,blank=True)
