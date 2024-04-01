from django.db import models

# Create your models here.
class Drmtm(models.Model):
    name=models.CharField(max_length=150)
    position=models.CharField(max_length=150)
    age=models.IntegerField()
    height=models.IntegerField()
    salary=models.IntegerField()