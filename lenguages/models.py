from django.db import models

# Create your models here.
class Paradigm(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Languague(models.Model):
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Programmer(models.Model):
    name = models.CharField(max_length=50)
    Languague = models.ManyToManyField(Languague)

    def __str__(self):
        return self.name
