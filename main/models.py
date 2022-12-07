from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2) # количество чисел до запятой -10,после -2
    quantity = models.IntegerField()
    description = models.TextField()
    status = models.CharField(max_length=15, choices=[('есть в наличии', 'in stock'), ('нет в наличии', 'out of stock') , ('ожидается', 'pending')])