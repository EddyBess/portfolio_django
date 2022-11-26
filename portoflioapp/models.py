from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    url = models.URLField()
    img = models.ImageField()

