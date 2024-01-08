from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medicines(models.Model):
    name=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    dosage=models.CharField(max_length=50)
    
    def _str_(self):
        return self.name