from email.headerregistry import Address
from django.db import models

# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    phno = models.BigIntegerField(editable=True)
    Address = models.CharField(max_length=500)



