from django.db import models

# Create your models here.
class Ninja(models.Model):
    name=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
