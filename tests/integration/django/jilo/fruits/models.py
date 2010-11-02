from django.db import models

class Eggplant(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    color = models.CharField(max_length=20, blank=True)
