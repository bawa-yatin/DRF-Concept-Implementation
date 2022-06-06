from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=150)


# Establishing Many-to-One Relationship
class Contact(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="contacts")

    # "to" describes the model we want to point to. "on_delete" instead describes how the database should behave when
    # the "one" side of the relationship is deleted. When the "one" entity is deleted, with CASCADE the "many"
    # entities are deleted as well. Let's say if a user is deleted then all contacts
    # related to it are also deleted
