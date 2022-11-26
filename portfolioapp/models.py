from django.db import models

# Create your models here.


class Images(models.Model):

    """Images Model allow possibilty to have images linked to skill/projects"""

    alt = models.CharField(max_length=50)
    img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.alt


class Skill(models.Model):

    """Skill Model represent a skill that is used in a project or mastered by the dev"""

    name = models.CharField(max_length=50)
    value = models.IntegerField(blank=True)
    img = models.ForeignKey("Images", on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Project(models.Model):

    """Project Model represent a project that has beeen made by the dev"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    date = models.DateField()
    url = models.URLField()
    skills = models.ManyToManyField(Skill)
    imgs = models.ManyToManyField(Images)

    def __str__(self):
        return self.name
