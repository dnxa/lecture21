from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)

    def __str__(self):
        return str(self.first_name)

class Book(models.Model):
    title = models.CharField(max_length=150)
    release_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.title)