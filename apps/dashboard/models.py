from django.db import models

# Create your models here.
# dashboard/models.py
from django.db import models

class Order(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
