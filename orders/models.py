from django.db import models


# Create your models here.
class DeviceType(models.Model):
    device_type_code = models.IntegerField()
    device_type_name = models.CharField(max_length=100)
