from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    publication_date=models.DateField()
    class Meta:
        db_table='custom_book_table'
