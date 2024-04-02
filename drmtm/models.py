from django.db import models

# Create your models here.
class Drmtm(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=150)
    position=models.CharField(max_length=150)
    age=models.IntegerField()
    height=models.IntegerField()
    salary=models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name