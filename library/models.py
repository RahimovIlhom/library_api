from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.IntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title
