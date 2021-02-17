from django.db import models
from django.contrib.postgres.fields import ArrayField

# Initially the application's database is centered around a single model, product
class Product(models.Model):
    picture = models.TextField()
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    link = models.TextField(blank=True)
    woman = ArrayField(models.CharField(max_length=20))
    occasion = ArrayField(models.CharField(max_length=20))
    profile = ArrayField(models.CharField(max_length=20))
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name
