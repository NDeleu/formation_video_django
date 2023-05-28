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
    
    -------------
    
    field = models.ManyToManyField()
    
    exemple : 
    class ModelA(models.Model):
        field = models.ManyToManyField(ModelB)
    soit un model A qui fait reference a un champ du model B
    
    exemple 2:
    class Book(models.Model):
        authors = models.ManyToManyField(Author)
    plusieurs auteurs potentiel d'un même livre
"""


class Author(models.Model):
    name = models.CharField(max_length=64, unique=True)


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True)
    quantity = models.IntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
