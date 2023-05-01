from django.db import models

# Create your models here.


class Employees(models.Model):
    full_name = models.CharField(max_length=40)
    position = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
