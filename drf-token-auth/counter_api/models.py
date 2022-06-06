from django.db import models


class Counter(models.Model):
    text = models.TextField()
    total_words = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.text
