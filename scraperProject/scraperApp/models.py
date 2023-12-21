from django.db import models

# Create your models here.
class Site(models.Model):
    address = models.CharField(max_length = 1000)
    name = models.CharField(max_length = 1000)
