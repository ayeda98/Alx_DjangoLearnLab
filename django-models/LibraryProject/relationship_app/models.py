from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    def __init__(self): 
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
   
class Library(models.Model):
    name =  models.CharField(max_length=200)
    books = models.ManyToManyField('Book')

class Librarian(models.Model):
    name =  models.CharField(max_length=200)
    Library = models.OneToOneField('Library', on_delete=models.CASCADE)
