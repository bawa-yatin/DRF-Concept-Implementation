from django.db import models


# Create your models here.

# Model for storing the user details
class Person(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.TextField(max_length=10)


# Model establishing one-to-one relation with the "Person" model indicating that
# every user will only have one Aadhar Card linked to it's profile
class Aadhar(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE, related_name="aadhar")
    sign = models.TextField()
    aadhar_no = models.TextField(max_length=12)