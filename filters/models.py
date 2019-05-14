from django.db import models


# Create your models here.
class Filter(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class NegativeFilter(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name