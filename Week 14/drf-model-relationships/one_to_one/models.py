from django.db import models


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.TextField(max_length=10)


class Aadhar(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE, related_name="aadhar")
    sign = models.TextField()
    aadhar_no = models.TextField(max_length=12)