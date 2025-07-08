from django.db import models

class Product (models.Model):
    ingredient = models.CharField(max_length=200)
