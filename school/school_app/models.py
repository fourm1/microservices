from django.db import models

class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    directorName = models.CharField(max_length=50)
