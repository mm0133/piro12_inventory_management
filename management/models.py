from django.db import models


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=20)
    content=models.TextField(default="")
    image = models.ImageField(upload_to = 'management', blank=True)
    price = models.IntegerField()
    number = models.IntegerField()
    client = models.ForeignKey('Client', on_delete=models.SET_NULL,null=True,  blank=True)


class Client(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    adress = models.CharField(max_length=100)
