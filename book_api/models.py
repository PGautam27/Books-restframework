from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    completed_reading = models.BooleanField()
    reading_platform = models.CharField(max_length=100)

    def __str__(self):
        return self.title
