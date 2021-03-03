from django.db import models


# Create your models here.
class EquipmentTypes(models.Model):
    type_name = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    uid = models.IntegerField(default=0)
    description = models.TextField(blank=True)
