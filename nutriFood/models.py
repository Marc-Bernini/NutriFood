from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=200)
    ingredient = models.CharField(max_length=500)
