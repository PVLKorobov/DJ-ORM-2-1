from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=50)


class Order(models.Model):
    products = models.ManyToManyField(Product, related_name='orders', through='OrderPosition')


class OrderPosition(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='positions')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='positions')
    quantity = models.IntegerField()