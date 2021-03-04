from django.db import models


# Create your models here.

class Cusstomers(models.Model):
    fio = models.CharField(max_length=100)
    organization_id = models.IntegerField(default=0)
    position = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    uid = models.IntegerField(default=0)