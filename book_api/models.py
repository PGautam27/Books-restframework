from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField()
    numberOfBooks = models.IntegerField()
    published_date = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
