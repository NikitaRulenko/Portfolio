from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Radiostation(models.Model):
    name = models.CharField(max_length=255)
    genre = models.ForeignKey('Genre', related_name='stations', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', related_name='stations', on_delete=models.CASCADE)
    adress = models.CharField(max_length=255)
    description = models.TextField

    def __str__(self):
        return self.name