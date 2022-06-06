from django.db import models


# Create your models here.
# Model for storing the names of different sauces
class Sauce(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model for storing the names of different sandwiches which can have multiple sauces
# and similarly multiple sandwiches can have the same one sauce
class Sandwich(models.Model):
    name = models.CharField(max_length=100)
    sauces = models.ManyToManyField(Sauce, related_name="sandwiches")

    def __str__(self):
        return self.name
