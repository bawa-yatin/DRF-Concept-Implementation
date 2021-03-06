from django.db import models


# Create your models here.

class GenericAuthor(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class GenericArticle(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('GenericAuthor', related_name='genericarticles', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
