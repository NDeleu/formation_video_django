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
    name = models.CharField(max_length=64, unique=True, verbose_name="Nom")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Auteur"
        verbose_name_plural = "Auteurs"


class Book(models.Model):
    title = models.CharField(max_length=32, unique=True, verbose_name="Titre")
    quantity = models.IntegerField(default=1, verbose_name="Quantité")
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, verbose_name="Auteur")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Livre"
        verbose_name_plural = "Livres"
