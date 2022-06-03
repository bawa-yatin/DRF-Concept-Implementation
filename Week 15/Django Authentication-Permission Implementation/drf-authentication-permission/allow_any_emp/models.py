from django.db import models


# Create your models here.
class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField()
    emp_mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.emp_name
