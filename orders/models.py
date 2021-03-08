from django.db import models


# Create your models here.
# todo luchanos ЭТО ТЕСТОВАЯ МОДЕЛЬ, ЧИСТО ПОКАЗАТЬ КАК РАБОТАЕТ РУЧКА И ВЗАИМОДЕЙСТВИЕ С БД
class DeviceType(models.Model):
    device_type_code = models.IntegerField()
    device_type_name = models.CharField(max_length=100)
