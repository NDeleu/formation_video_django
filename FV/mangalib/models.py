from django.db import models

"""
    primary_key
    unique
    default
    null
    blank
    
    CharField
    IntegerField
    DateField
    DateTimeField
    FloatField
    EmailField
    BooleanField
"""


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    quantity = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
