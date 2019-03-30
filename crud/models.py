from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.CharField(max_length=30)
    publication = models.CharField(max_length=2)