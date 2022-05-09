from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.CharField(max_length=10)
    publish_date = models.DateField()
    quantity = models.CharField(max_length=10)

    def __str__(self):
        return self.title
