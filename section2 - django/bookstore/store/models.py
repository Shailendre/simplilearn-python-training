from django.db import models

"""
    This is plain Python Object. this model is similar to Entity object in JPA context
"""

# Create your models here.
class Book(models.Model):
    """docstring for book model"""
    # added in 0001 migration
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=45)
    description = models.TextField()
    published_date = models.DateField()
    # added in 0002 migraation
    price = models.DecimalField(decimal_places=2, max_digits=6)
    stock = models.IntegerField(default=0)
