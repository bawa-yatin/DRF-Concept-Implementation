from django.db import models


# Create your models here.

# Model for storing the names of users
class User(models.Model):
    username = models.CharField(max_length=150)


# Model for establishing Many-to-One Relationship with the "User" model indicating
# that a user can have multiple email addresses
class Contact(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="contacts")

    # "to" describes the model we want to point to. "on_delete" instead describes how the database should behave when
    # the "one" side of the relationship is deleted. When the "one" entity is deleted, with CASCADE the "many"
    # entities are deleted as well. Let's say if a user is deleted then all contacts
    # related to it are also deleted
