from django.db import models


# Create your models here.
class DeviceType(models.Model):
    device_type = models.IntegerField()
    device_type_name = models.CharField(max_length=100)



class NewOrders(models.Model):
    status_order = models.IntegerField(default=0)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    uid = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    customer_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    order_type = models.IntegerField(default=0)
