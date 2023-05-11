from django.db import models

# Create your models here.

#primeira coisa a se fazer em bancos

class DataValue(models.Model):
    value = models.IntegerField()
    day = models.CharField(max_length=100, default=None)

