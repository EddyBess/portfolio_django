from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(blank=True)
    img = models.ImageField(blank=True)
    def __str__(self):
        return self.name
class Project(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    url = models.URLField()
    skills = models.ManyToManyField(Skill)

    def __str__(self):
        return self.name

