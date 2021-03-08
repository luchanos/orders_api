from django.db import models


# Create your models here.
# todo luchanos ЭТО ТЕСТОВАЯ МОДЕЛЬ, ЧИСТО ПОКАЗАТЬ КАК РАБОТАЕТ РУЧКА И ВЗАИМОДЕЙСТВИЕ С БД
class DeviceType(models.Model):
    device_type_code = models.IntegerField()
    device_type_name = models.CharField(max_length=100)


class Cusstomers(models.Model):
    fio = models.CharField(max_length=100)
    organization_id = models.IntegerField(default=0)
    position = models.CharField(max_length=100)
    created_dt = models.DateTimeField(auto_now_add=True)
    updated_dt = models.DateTimeField(auto_now=True)
    uid = models.IntegerField(default=0)