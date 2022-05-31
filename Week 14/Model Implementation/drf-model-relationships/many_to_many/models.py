from django.db import models


# Create your models here.

class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    sauces = models.ManyToManyField(Sauce, related_name="sandwiches")

    def __str__(self):
        return self.name
