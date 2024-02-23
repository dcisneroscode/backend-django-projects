from django.db import models


# Author Models
class Author(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    
    def __str__(self):
        return self.name

# Book Models
class Book(models.Model):
    title = models.CharField(max_length=200)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
