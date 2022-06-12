
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PFE(models.Model):
    institue = models.CharField(max_length=60 , blank=True )
    anneScolere = models.CharField(max_length=9 , blank=True)
    cin = models.IntegerField(max_length=8 , blank=True)
    nomEtudian = models.CharField(max_length=60  ,  blank=True)
    uniqueID = models.CharField(max_length=100 , unique=True , blank=True , null=True )
    file = models.FileField()
  
    def __str__(self):  
        return str(self.nomEtudian)