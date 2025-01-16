from django.db import models
from django.db.models import CharField


class Student(models.Model):
    name = models.CharField(max_length=50)
    genre = models.BooleanField()
    school_id = CharField(null=False, blank=False, max_length=100)